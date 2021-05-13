N = int(input())
a = list(map(int, input().split()))
j = 1
for i in range(N):
  if a[i] == j:
    j += 1
    ans = N-j+1
if j == 1:
  ans = -1
print(ans)