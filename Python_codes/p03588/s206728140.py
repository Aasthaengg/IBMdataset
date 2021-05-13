N = int(input())
ans = [-1, -1]
for i in range(N):
  A, B = map(int, input().split())
  if A > ans[0]:
    ans[0] = A
    ans[1] = A + B
print(ans[1])