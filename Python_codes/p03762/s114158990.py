n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

q = 10**9+7

x_sum = 0
y_sum = 0
for i in range(n):
    x_sum += (2*i - n + 1) * x[i]
    
for i in range(m):
    y_sum += (2*i - m + 1) * y[i]

print(  ((x_sum * y_sum )%q) )