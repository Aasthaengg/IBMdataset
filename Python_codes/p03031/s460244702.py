n,m=map(int,input().split())
s=[]
for i in range(m):
  inp=list(map(lambda x:int(x)-1,input().split()))
  s.append(inp[1:])
p=list(map(int,input().split()))
c=0
for i in range(2**n):
  st=[]
  for j in range(m):
    t=0
    for k in s[j]:
      if i&(2**k):
        t^=1
    st.append(t)
  if p==st:
    c+=1
print(c)