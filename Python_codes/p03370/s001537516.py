n, x = map(int, input().split())
m = [int(input()) for i in range(n)]
sum = 0
for i in range(n):
    sum+=m[i]
x-=sum
print(n+int(x/min(m)))