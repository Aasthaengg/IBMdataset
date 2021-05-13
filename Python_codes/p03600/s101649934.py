# ABC074D
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



def main():
    n = int(input())
    d = [None]*n

    for i in range(n):
        d[i] = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(n):
                if k in (i,j):
                    continue
                if (d[i][j]>d[i][k]+d[j][k]) or (d[i][k]>d[i][j]+d[j][k]) or (d[k][j]>d[i][k]+d[j][i]):
                    print(-1)
                    return
                if d[i][j]==d[i][k]+d[j][k]:
                    break
            else:
                ans += d[i][j]
    print(ans)
main()