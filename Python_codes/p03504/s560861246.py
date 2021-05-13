import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main():
    n,c = map(int,input().split())
    time = [[0] * c for _ in range(10 ** 5 + 1)]

    for _ in range(n):
        s,t,c1 = map(int,input().split())
        c1 -= 1
        time[s][c1] += 1
        time[t][c1] -= 1
    
    for i in range(10 ** 5):
        for j in range(c):
            if time[i][j] == 0 and time[i + 1][j] == 1:
                time[i][j] = 1
                time[i + 1][j] = 0

    ans = sum(time[0])
    tmp = ans
    for i in range(1,10 ** 5 + 1):
        tmp += sum(time[i])
        ans = max(ans, tmp)
    
    print(ans)
if __name__=='__main__':
    main()

