import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    S = input()
    ans = 0
    for i in range(n-1):
        l = S[:i+1]
        r = S[i+1:]
        cnt = 0
        for s in set(l):
            if r.find(s) >= 0:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()