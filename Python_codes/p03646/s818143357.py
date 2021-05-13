k=int(input())
arr=[0]*50
for i in range(50):
  if k%50==0:
    arr[i]+=50*min(1,k)+max((k//50-1),0)
  else:
    if i<=(k%50-1):
      if k<50:
        arr[i]+=50
      else:
        arr[i]+=50+(k//50)
    else:
      if k<50:
        arr[i]=0
      else:
        arr[i]+=50+(k//50-1)-k%50
print(50)
print(*arr)