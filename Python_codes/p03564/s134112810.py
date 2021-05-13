N=int(input())
K=int(input())
a=[1,2]
for i in range(2,N+1):
    if a[i-1]<K:
        a.append(a[i-1]*2)
    else:
        a.append(a[i-1]+K)
print(a[N])