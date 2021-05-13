I = [int(_) for _ in open(0).read().split()]
n, u, v = I[:3]
A, B = I[3::2], I[4::2]
S = [set() for _ in range(n+1)]
for a, b in zip(A, B):
    S[a].add(b)
    S[b].add(a)
def cal(x):
  dist=[None]*(n+1)
  dist[x]=0
  st=set([x])
  while st:
    x=st.pop()
    for i in S[x]:
      if dist[i]==None:
        dist[i]=dist[x]+1
        st.add(i)
  return dist

T=cal(u)
A=cal(v)
ans=0
for t,a in zip(T[1:],A[1:]):
  if t<a:
    ans=max(ans,a-1)
print(ans)