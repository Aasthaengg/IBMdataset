N=int(input())
if N%2==1:
  print(0)
else:
  divide=2
  count=0
  while divide<N:
    divide*=5
    count+=N//divide
  print(count)  