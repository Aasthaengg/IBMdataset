N=int(input())
ls=list(input())
left=0
right=N-1
count=0
while True:
  while left<N and ls[left]=='R':
    left+=1
  while right>0 and ls[right]=='W':
    right-=1
  if left>=right:
    break
  left+=1
  right-=1
  count+=1
print(count)