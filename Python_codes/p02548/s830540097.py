N = int(input())
ans = 0
for n in range(1,N):
  ans += int((N-1)/n)
print(ans)