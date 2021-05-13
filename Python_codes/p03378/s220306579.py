N,M,X=map(int,input().split())
List = list(map(int, input().split()))
pattern1 = 0
pattern2 = 0
setCost = set(List)
for i in range(N):
  if i in setCost:
    pattern1 += 1
  if i == X:
    break
for j in range(N,0,-1):
  if j in setCost:
    pattern2 += 1
  if j == X:
    break
if pattern1 < pattern2:
  print(pattern1)
else:
  print(pattern2)