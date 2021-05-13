import sys
def input(): return sys.stdin.readline().rstrip()
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())

def main():
    mod = 10**9+7
    n = ii()
    a = li()
    bi = [0]*60
    for x in a:
        for i in range(60):
            if (x>>i)&1:
                bi[i]+= 1
    ans = 0
    for i in range(60):
        tmp = bi[i]*(n-bi[i])*(1<<i)
        tmp %= mod
        ans += tmp
        ans %= mod

    print(ans)



if __name__ == '__main__':
    main()