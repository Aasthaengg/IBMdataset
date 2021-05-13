N = int(input())
A = [int(a) for a in input().split()]
ans = 0
i = 0
while i < N-1:
  if A[i] == A[i+1]:
    ans += 1
    i += 2
  else:
    i += 1
    
print(ans)