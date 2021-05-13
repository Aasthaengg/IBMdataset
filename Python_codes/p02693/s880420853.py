k=int(input())
a,b=map(int,input().split())

for i in range(1,1001):
  n=k*i
  if a<=n<=b:
    print('OK')
    exit()
  else:
    continue

print('NG')


