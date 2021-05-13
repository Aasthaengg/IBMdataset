a, b, c = map(int, input().split())
k = int(input())
m = max({a, b, c})
t = m
for i in range(k): m*=2
print(a+b+c-t+m)