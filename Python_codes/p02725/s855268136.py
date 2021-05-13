k,n = map(int,input().split())

a = list(map(int,input().split()))

b = []

for i in range(n-1):
    b += [a[i+1] - a[i]]
b += [k - a[n-1] + a[0]]

print(k-max(b))
