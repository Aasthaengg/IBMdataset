import sys
n = int(input())
l = [int(x) for x in input().split()]
l.sort()
for i in range(n):
  if(i == n-1):
    continue
  elif(l[i] == l[i + 1]):
    print('NO')
    sys.exit()
print('YES')    
