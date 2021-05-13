A, B, C = [int(x) for x in input().strip().split()]
ans = min(B, C) * 2
B -= ans // 2
C -= ans // 2
ans += B
ans += min(A, C)
C -= A
if C > 0:
  ans += 1
print(ans)