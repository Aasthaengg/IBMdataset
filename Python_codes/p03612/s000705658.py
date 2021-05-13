import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    p = LI()
    ans = 0
    for i in range(1, n):
        if p[i-1] == i:
            temp = p[i-1]
            p[i-1] = p[i]
            p[i] = temp
            ans += 1
    if p[n-1] == n:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()