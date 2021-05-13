n,a,b = map(int,input().split())
x_ls = list(map(int, input().split()))

cost = 0
for i in range(1,n):
    diff = x_ls[i] - x_ls[i-1]
    if diff * a < b:
        cost += diff * a
    else:
        cost += b
print(cost)