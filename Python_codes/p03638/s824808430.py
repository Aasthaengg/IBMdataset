h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

i=-1
j=0
ans=[]
for x in range(h):
  l=[]
  for y in range(w):
    i+=1
    if i==a[j]:
      i=0
      j+=1
    l.append(j+1)
  ans.append(l)
for i in range(0,len(ans),2):
  ans[i].reverse()
print("\n".join(map(lambda x:" ".join(map(str,x)),ans)))
