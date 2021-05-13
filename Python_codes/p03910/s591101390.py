n=int(input())
c=0
while (c+1)*c/2<n:
  c+=1
for i in range(1,c+1):
  if i!=c*(c+1)/2-n:
    print(i)