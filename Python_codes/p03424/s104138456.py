N=int(input())
A=list(map(str, input().split()))
color=['P','W','G','Y']
counter=0
for i in color:
  if i in A:
    counter+=1
if counter==4:
  print('Four')
else:
  print('Three')
