S = int(input())
total=0
for i in range(S):
  l,r = map(int,input().split())
  total+=r-l
print(total+S)