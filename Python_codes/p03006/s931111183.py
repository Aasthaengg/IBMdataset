from collections import defaultdict
dic = defaultdict(int) #初期化する関数。

N = int(input())
if N == 1:
  print(1)
  exit()
X = []
for i in range(N):
  x,y = map(int,input().split())
  X.append([x,y])

for i in range(N):
  for j in range(i+1,N):
    p = X[i][0] - X[j][0]
    q = X[i][1] - X[j][1]
    if p <0:
      p = -p;q=-q
    if p == 0 and q < 0:
      q=-q
    dic[(p,q)] +=1

path = max(dic.values())
ans = N-path
#print(dic)
print(ans)