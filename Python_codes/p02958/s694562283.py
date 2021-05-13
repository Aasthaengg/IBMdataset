N=int(input())
List = list(map(int, input().split()))
flag = 0
for i in range(N):
  if List[i] == i+1:
    pass
  else:
    flag += 1
if flag==2 or flag == 0:
  print("YES")
else:
  print("NO")