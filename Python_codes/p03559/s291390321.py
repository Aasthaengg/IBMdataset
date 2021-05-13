import bisect
n=int(input())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
a.sort()
b.sort()
c.sort()


ans=0
ind=[0]
for i in range(n):
  ind.append(n-bisect.bisect_right(c,b[i])+ind[i])

for i in a:
  b_ind=bisect.bisect_right(b,i)

  ans+=ind[n]-ind[b_ind]

print(ans)