n =int(input())
t,a =map(int,input().split())
h = list(map(int,input().split()))
ans = 0
near = 10000
for i in range(n):
    if abs(t-h[i]*0.006 - a) < near:
        ans = i
        near = abs(t-h[i]*0.006-a)
print(ans+1)