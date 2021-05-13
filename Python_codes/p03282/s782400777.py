s=input()
k=int(input())
for i in s:
  if i!='1':
    print(i)
    break
  else:
    k-=1
    if k==0:
      print(i)
      break