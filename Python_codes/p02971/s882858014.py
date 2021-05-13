n=int(input())
arr=[0]*n
for i in range(n):
  arr[i]=int(input())
tmp=sorted(arr,reverse=True)
arrMax=tmp[0]
for i in range(n):
  if arr[i]==arrMax:
    if tmp[0]==tmp[1]:
      print(tmp[0])
    else:
      print(tmp[1])
  else:
    print(tmp[0])

  
