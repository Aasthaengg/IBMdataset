n = int(input())
a = [int(input()) for _ in range(n)]
pl = [-1]*(n+1)

for i in range(n):
    pl[a[i]-1] = i

a = 1
ma = 1
for i in range(n):
    if pl[i] < pl[i+1]:
        a += 1
    else:
        ma = max(a,ma)
        a = 1
        
print(n-ma)