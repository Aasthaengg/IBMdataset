N,T = map(int,input().split())

ans = -1
cost = 10**5

for i in range(0,N,1):
    c,t = map(int,input().split())
    if t <= T and c < cost:
        cost =c
        ans = i+1

print(cost if ans != -1 else "TLE")
