s=input()
n=len(s)
w=int(input())
n=(n+w-1)//w
l,r=0,w
a=[]
for i in range(n):
  t=""
  if i==n-1:
    t=s[l:]
    a.append(t[0])
    continue
  t=s[l:r]
  a.append(t[0])
  l=r
  r+=w
print("".join(a))
