n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
sum = 0
min = 1000000
for i in range(n):
    sum+=m[i]
    if min > m[i]: min = m[i]
x-=sum
print(n+int(x/min))