A = int(input())
B = int(input())
C = int(input())
X = int(input())
X = X // 50

ans = 0
for ai in range(A+1):
  for bi in range(B+1):
    for ci in range(C+1):
      if 10*ai + 2*bi + ci == X:
        ans += 1
        
print(ans)
