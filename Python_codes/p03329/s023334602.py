n=int(input())

sub=[1,6,9,36,81,216,729,1296,6561,7776,46656,59049]
cost=[0]*(n+1)
for i in range(n+1):
    cost[i]=i
for i in range(n+1):
    for j in range(len(sub)):
        if sub[j]<=i:
            cost[i]=min(cost[i], cost[i-sub[j]]+1)
        else:
            break
print(cost[n])
