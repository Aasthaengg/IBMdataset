n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

ans,num = [],0
for i in range(n):
    num += abs(x[i] - y[i])
ans += num,

num = 0
for i in range(n):
    num += (x[i] - y[i])**2
num **= 1/2
ans += num,

num = 0
for i in range(n):
    num += (abs(x[i] - y[i]))**3
num **= 1/3
ans += num,

num = []
for i in range(n):
    num += abs(x[i] - y[i]),
num = max(num)
ans += num,

print(*ans, sep = "\n")
