import collections
n,k = map(int,input().split())

a = list(map(int,input().split()))

b = collections.Counter(a)
b = sorted(b.items(), key=lambda x:x[1])
c = set(a)

if len(c) <= k:
    print(0)
else:
    ans = 0
    b = b[:len(b)-k]
    for i in b:
        ans +=i[1]
        
    print(ans)        