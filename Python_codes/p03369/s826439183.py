S=list(input())
count=0

for i in S:
  if i=='o':
    count+=1

fee=700+100*count

print(fee)