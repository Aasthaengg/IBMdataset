N = int(input())
A,B = map(str,input().split())

ans = ''

for i in range(N):
  ans = ans + A[i] + B[i]
  
print(ans)