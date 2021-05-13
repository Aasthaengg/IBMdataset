n = int(input())
value = list( map( int, input().split() ) )
cost = list( map( int, input().split() ) )

ans = 0
for i in range(n):
    x = value[i]-cost[i]
    if x > 0:
        ans += x
print(ans)
