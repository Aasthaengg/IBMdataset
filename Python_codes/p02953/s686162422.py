N=int(input())
List = list(map(int, input().split()))
flg = True
if N ==1: print("Yes")
else:
  for i in range(1,N):
    if List[i]==List[i-1]:
      pass
    elif List[i]>List[i-1] or List[i]-1>=List[i-1]:
      List[i] = List[i]-1
    else:
      flg=False
      break
  if flg:
    print("Yes")
  else:
    print("No")