a,b=input().split()
c = int(a+b)
for i in range(1, 350):
  if c == i*i:
    print('Yes')
    exit()
print('No')
