from collections import Counter

count_by_kw = Counter()

n=int(input())
l=[]
dict={}
ans=0
for x in range(n):
  a=sorted(input())
  b=''.join(a)
  if not b in dict:
    dict[b]=x
    l.append(b)
    count_by_kw[b]+=1
  else:
    d=count_by_kw[b]
    count_by_kw[b]+=1
    
for y in range(len(l)):
  r=l[y]
  w=count_by_kw[r]
  ans+=w*(w-1)//2

print(ans)


