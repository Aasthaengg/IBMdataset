a,b,c=map(int,input().split())

res=c
for i in range(10000):
  res += b
  if res % a==0:
    print('YES')
    exit()
    
print('NO')