n = int(input())
A = sorted(set(map(int, input().split())))

ans = 0

for a_i in range(1, len(A)):
  ans += A[a_i]-A[a_i-1]
  
print(ans)