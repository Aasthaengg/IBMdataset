N = int(input())

value = list(map(int,input().split()))

cost = list(map(int,input().split()))

sum = 0
for i in range(N) :
    if value[i] >= cost[i] : 
        sum = sum + value[i] - cost[i]

print(sum)