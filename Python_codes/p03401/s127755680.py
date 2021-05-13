n = int(input())
x = list(map(int,input().split()))
x = [0]+x+[0]
cost = 0
for i in range(n+1):
    cost+=abs(x[i]-x[i+1])
for i in range(1,n+1):
    cost2 = cost - abs(x[i]-x[i-1]) - abs(x[i]-x[i+1]) + abs(x[i-1]-x[i+1])
    print(cost2)
