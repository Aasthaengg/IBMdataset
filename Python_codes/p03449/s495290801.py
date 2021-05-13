n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = 0
for i in range(n):
    c = sum(a[0:i+1]) + sum(b[i:n])
    t = max(t,c)

print(t)