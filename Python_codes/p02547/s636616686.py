n = int(input().strip())
count = 0
for i in range(n):
  a,b = map(int,input().strip().split())
  if count == 3:
    print('Yes')
    exit(0)
  elif a == b:
    count += 1
  elif(a != b):
    count = 0
if count == 3:
	print('Yes')
else:
	print('No')
