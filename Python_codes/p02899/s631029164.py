N=int(input())
List = list(map(int, input().split()))
resList = [0]*N
for i in range(N):
  resList[List[i]-1] = i+1
print(*resList)