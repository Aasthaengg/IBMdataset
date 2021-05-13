n,m=[int(x) for x in input().rstrip().split()]
a=[int(x) for x in input().rstrip().split()]
a.sort(reverse=True)
d=[]
bc=[]
for i in range(m):
  b,c=[int(x) for x in input().rstrip().split()]
  bc.append([b,c])

cnt=0
bc.sort(key=lambda x:x[1],reverse=True)
for b,c in bc:

  d.extend([c]*b)
  cnt+=b
  if n<cnt:
    break
  
d.sort(reverse=True)
a+=d
a.sort(reverse=True)
print(sum(a[:n]))
