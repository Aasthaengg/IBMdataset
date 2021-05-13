from collections import deque
h,w=map(int,input().split())
s=[input() for _ in range(h)]
vi=[ [-1 for _ in range(w)] for _ in range(h)]
st=deque()
st.append([0,0,0])


d=[[0,1],[-1,0],[1,0],[0,-1]]
while st:
  h1,w1,i=st.popleft()

  if 0<=h1<h and 0<=w1<w and vi[h1][w1]==-1 and s[h1][w1]==".":
    vi[h1][w1]=i+1
    for m in d:
      st.append([h1+m[0],w1+m[1],i+1])

print("".join(s).count(".")-vi[h-1][w-1] if vi[h-1][w-1]!=-1 else -1)
