k,n = map(int,input().split())
a = list(map(int,input().split()))

b = []
for i in range(n-1):
    kyori = a[i+1] - a[i]
    b.append(kyori)
b.append(abs(a[0]+(k-a[-1])))

print(sum(b)-max(b))
