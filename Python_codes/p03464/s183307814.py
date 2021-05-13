K=int(input())
A=input().split(' ')
min=2
max=2
flag=0
while K>0:
  K=K-1
  i=int(A[K])
  if max<i:
    print('-1')
    flag=1
    break
  elif i<min:
    if min%i!=0:min=min+i-(min%i)
    else:min=min+(min%i)
    max=max+i-(max%i)-1
    if min>max:
      print('-1')
      flag=1
      break
  else:
    min=i
    max=max+i-(max%i)-1
if flag==0:
  print('{0} {1}'.format(min,max))