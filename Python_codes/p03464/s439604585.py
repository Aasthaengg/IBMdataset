k = int(input())
A = list(map(int,input().split()))

ans = [2,2]
for a in A[::-1]:

  if a > ans[1]:
    print(-1)
    exit()
  ans[1] = (ans[1]//a) *a+ (a-1)
  if ans[0] <= a:
    ans[0] = a
  else:
    if ans[0]%a != 0:
      ans[0] = (ans[0]//a+1)*a
  if ans[0] >ans[1]:
    print(-1)
    exit()
print(*ans)