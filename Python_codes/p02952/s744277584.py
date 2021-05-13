N=int(input())
count=0
for i in range(N):
  i=str(i+1)
  lst=list(map(int,i))
  if len(lst)%2==1:
    count+=1
print(count)