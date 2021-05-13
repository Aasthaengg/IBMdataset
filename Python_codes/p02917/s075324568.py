N = int(input())
B = list(map(int, input().split()))
ans = 0
ans += B[0]
ans += B[N-2]
for i in range(N-2):
  if B[i] <= B[i+1]:
    ans += B[i]
  else:
    ans += B[i+1]
print(ans)