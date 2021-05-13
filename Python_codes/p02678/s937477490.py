from collections import deque
n,m=map(int,input().split())
l=[[0] for _ in range(n+1)]
vi=[0 for _ in range(n+1)]

for i in range (m):
  a,b=map(int,input().split())
  l[a].append(b)
  l[b].append(a)
st=deque([1])
f=set([1])


while st:
  x=st.popleft()
  for k in l[x]:
    if k not in f:
      st.append(k)
      f.add(k)
      vi[k]=x   
  
print("Yes")
for m in vi[2:]:
  print(m)
  
  
