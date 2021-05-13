from collections import deque
h,w=map(int,input().split())
s=[input() for _ in range(h)]
vi=[ [-1 for _ in range(w)] for _ in range(h)]
st=deque()
st.append([0,0,1])
vi[0][0]=1
while st:
  h1,w1,i=st.popleft()
  d=[[0,1],[-1,0],[1,0],[0,-1]]
  for m in d:
    if h1+m[0]==h-1 and w1+m[1]==w-1:
      vi[h-1][w-1]=i+1
      st.clear()
    if 0<=h1+m[0]<h and 0<=w1+m[1]<w:
      if vi[h1+m[0]][w1+m[1]]==-1 and s[h1+m[0]][w1+m[1]]==".":
        st.append([h1+m[0],w1+m[1],i+1])
        vi[h1+m[0]][w1+m[1]]=i+1

print("".join(s).count(".")-vi[h-1][w-1] if vi[h-1][w-1]!=-1 else -1)
