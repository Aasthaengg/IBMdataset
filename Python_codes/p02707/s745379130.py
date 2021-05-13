N=int(input())
List = list(map(int, input().split()))
resList=[0]*N
for i in range(N-1):
  resList[List[i]-1]+=1
for res in resList:
  print(res)