N = int(input())
a = list(map(int,input().split()))
count = 0

for i in a:
  if i%2==0:
    K=True
    while K:
      if i%2!=1:
        i//=2
        count+=1
      else:
        K =False
          
print(count)