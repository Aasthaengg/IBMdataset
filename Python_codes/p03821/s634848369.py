N =int(input())
a = [0] * N
b = [0] * N
for i in range(N):
    A, B = map(int, input().split())
    a[i], b[i] = A, B
    
ans = 0
for i in range(N-1,-1,-1):
  if (a[i]+ans)%b[i]==0:
    push = 0
  else:
    push = b[i] - (a[i]+ans)%b[i]
  ans += push
print(ans)