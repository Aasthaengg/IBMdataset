n = int(input())
A = list(map(int, input().split()))
absA = [abs(a) for a in A]

if sum(True if a < 0 else False for a in A) % 2 == 0:
  ans = sum(absA)
else:
  ans = sum(absA) - 2 * min(absA)
  
print(ans)