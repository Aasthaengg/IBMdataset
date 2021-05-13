n=int(input())
li=sorted(list(map(int,input().split())))
bef=-1

for i in li:
  if bef==i:
    print("NO")
    break
  bef=i
else:
  print("YES")
