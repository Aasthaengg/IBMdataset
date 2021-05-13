a,b=map(int,input().split());count=0
for i in range(a,b+1):
  c=str(i)
  if c==c[::-1]: count+=1
print(count)