n= int(input())
a = list(map(int,input().split()))
score=1
if 0 in a:
  print(0)
  exit()
for i in a:
  score*=i
  if score>10**18:
    print(-1)
    exit()
print(score)