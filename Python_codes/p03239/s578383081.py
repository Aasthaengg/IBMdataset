N,T = map(int,input().split())
cost = "TLE"
for i in range(N):
    c,t = map(int,input().split())
    if t <= T:
        if cost == "TLE":
            cost = c
        else:
            if cost > c:
                cost = c

print(cost)
