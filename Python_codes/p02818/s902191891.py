a,b,k = map(int, input().split())

t = a - min(a,k)
k -= min(a,k)
q = b - min(k,b)

print(t,q)