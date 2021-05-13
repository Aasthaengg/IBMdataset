tmp = input().split()
val = [int(v) for v in tmp]
if val[0] * val[1] >= val[2]:
  ans = val[2]
else:
  ans = val[0] * val[1]
print(ans)