N = int(input())

ans = 0
for i in range(1, N):
  if ((N-i)%i==0) and (i<(N-i)//i):
    ans += (N-i)//i
  elif i > (N-i)//i:
    break
print(ans)