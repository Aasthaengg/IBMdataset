N = int(input())

a = list(map(int,input().split()))
s = sum(a)
l = a[0]
m = abs((s-l)-l)
for i in range(1,N-1):
    l += a[i]
    m = min(m,abs((s-l)-l))
print(m)