N = int(input())
ans = 0
kotai = 1
while N >= 1:
  ans += kotai
  N = N//2
  kotai *= 2
print(ans)