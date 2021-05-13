n = int(input())
a = [0]+list(map(int,input().split()))
x = [0]*(n+1)
for i in range(n,0,-1):
    buf = 0
    for j in range(1,n//i+1):
        buf += x[i*j]
    if buf%2!=a[i]:x[i]=1
x = x[1:]
m = 0
b = []
for i in range(n):
    if x[i]==1:
        b.append(i+1)
        m+=1
print(m)
print(*b)

