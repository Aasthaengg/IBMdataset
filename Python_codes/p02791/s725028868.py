N = int(input())
P = list(map(int,input().split()))
Min = P[0]
cnt = 0
for Pi in P:
    if Pi <= Min:
        Min = Pi
        cnt +=1
print(cnt)