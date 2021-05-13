n = int(input())
ab = []
A = 0

for i in range(n):
  a,b = map(int,input().split())
  ab.append([b,a])

ab.sort()

for j in range(n):
  A += ab[j][1]
  if A>ab[j][0]:
    print('No')
    exit()
    
print('Yes')