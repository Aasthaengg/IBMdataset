A,B,C=map(int,input().split())
for i in range(1,10**5):
  if (B*i+C)%A==0:
    print('YES')
    break
else:
  print('NO')