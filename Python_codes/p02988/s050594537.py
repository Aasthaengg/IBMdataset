n=int(input())
list=list(map(int, input().split()))
count=0
for i in range(n-2):
  l=[list[i],list[i+1],list[i+2]]
  l.sort()
  if l[1]==list[i+1]:
    count+=1
print(count)
