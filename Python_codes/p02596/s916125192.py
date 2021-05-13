k=int(input())
x=0
for i in range(k):
  x*=10
  x+=7
  if x%k==0:
    print(i+1)
    exit()
  x%=k
print(-1)