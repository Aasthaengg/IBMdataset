n,k=map(int,input().split())
a=list(map(int,input().split()))
import collections

a=collections.Counter(a)
key=list(a.values())
key.sort()
ans=sum(key[:len(key)-k])
print(ans)
