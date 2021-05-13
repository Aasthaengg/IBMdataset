N = int(input())
A = list(map(int,input().split()))

ans = 1
if any(j == 0 for j in A) == True:
    ans = 0
else:
  for i in A:
    ans *= i
    if ans > 10**18:
      ans = -1
      break

print(ans)