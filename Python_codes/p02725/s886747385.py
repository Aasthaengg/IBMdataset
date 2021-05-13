K,N=map(int,input().split())
List = list(map(int, input().split()))
res = 0
mid = 0
for i in range(N):
  if i == N-1:
    res+= K-List[i]+List[0]
    mid = max(mid,K-List[i]+List[0])
  else:
    res+= List[i+1]-List[i]
    mid = max(mid,List[i+1]-List[i])
res = res - mid
print(res)