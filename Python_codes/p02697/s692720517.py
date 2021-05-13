MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

def main():
    n,m = map(int,input().split())
    ans = [[0]*2 for _ in range(m)]
    cnt = 1
    if n%2 == 1:
        for i in range(m):
            ans[i][0] = cnt
            cnt += 1
        for i in range(m - 1,-1,-1):
            ans[i][1] = cnt
            cnt += 1
        for i in range(m):
            print(*ans[i])
    else:
        for i in range(m):
            ans[i][0] = cnt
            cnt += 1
        cnt = n
        flag = True
        for i in range(m):
            if flag and cnt - ans[i][0] <= n//2:
                flag = False
                cnt -= 1
            ans[i][1] = cnt
            cnt -= 1
        for i in range(m):
            print(*ans[i])
if __name__ == '__main__':
    main()
