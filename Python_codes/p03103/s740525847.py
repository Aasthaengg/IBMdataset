import numpy as np

def solve():
    cnt = 0
    money = 0
    for i in range(N):
        if cnt >= M:
            break
        if cnt + AB[i][1] >= M:
            money += AB[i][0] * (M - cnt)
            cnt = M   
        else:
            money += AB[i][0]*AB[i][1]
            cnt += AB[i][1]
#    print(cnt)
    print(money)

if __name__ == "__main__":
    N,M = list(map(int, input().split()))   
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
#    print(AB)
    solve()
