n, a, b = map(int, input().split())

x = list(map(int, input().split())) 

cost = 0
for i in range(n-1):
    length = x[i+1] - x[i]
    if length*a < b:
        cost += length*a
    else:
        cost += b
print(cost)