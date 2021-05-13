n = int(input())
p = [int(input()) for i in range(n)]

a = [0 for i in range(n)]

for i in range(n):
    a[p[i]-1]=i+1

b = [1]
for i in range(1,n):
    if a[i-1]<a[i]:
        b[-1]+=1
    else:
        b.append(1)
print(n-max(b))
