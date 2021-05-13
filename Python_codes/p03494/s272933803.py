n=int(input())
a=list(map(int,input().split()))
count=-1
for j in range(10**5):
  count+=1
  for i in range(n):
    if a[i]%2!=0:
      print(count)
      exit()
    a[i]//=2
  
print(count)