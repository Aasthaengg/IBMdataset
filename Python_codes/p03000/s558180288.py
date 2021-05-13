N,X=map(int,input().split())
List = list(map(int, input().split()))
height = 0
res = 1
def checkF(k,x):
  if k>x:
    return True
  else:
    return False
    
for i in range(N):
  height += List[i]
  res +=1
  if checkF(height,X):
    res = res-1
    break
print(res)