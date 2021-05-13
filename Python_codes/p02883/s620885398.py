n,k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

k = max(sum(a)-k,0)

a.sort()
f.sort()
f.reverse()

# rは100%満たす。lは100%満たさない
l = -1
r = a[-1]*f[0]*2

while l+1!=r:
    x = (l+r)//2
    b = []
    for i in range(n):
        b.append(min(x//f[i], a[i]))
    if k<=sum(b):
        r=x
    else:
        l=x

print(r)