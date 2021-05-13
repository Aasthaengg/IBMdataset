road=[0]*5
corr=[0,1,2,2,1]
for _ in range(3):
  a,b=map(int,input().split())
  road[a]+=1
  road[b]+=1
print("YES" if road==corr else "NO")
