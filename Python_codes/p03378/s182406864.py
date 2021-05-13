n,m,x = map(int,input().split())

a = list(map(int,input().split()))

cost = [0,0]

for i in a:
    if i < x:
        cost[0] += 1
    else:
        cost[1] += 1
print(min(cost))