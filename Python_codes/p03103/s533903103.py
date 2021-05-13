import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, m = MI()
    a_b = [LI() for _ in range(n)]
    a_b.sort(key=lambda x:x[0])
    cnt = 0
    ans = 0
    for i in range(n):
        a = a_b[i][0]
        b = a_b[i][1]
        if cnt + b < m:
            cnt += b
            ans += a*b
        else:
            ans += a*(m - cnt)
            break
    print(ans)

if __name__ == '__main__':
    main()