A, B = map(lambda x: int(x) - 1, input().split())

if B == 0:
  ans = 0
elif B % A == 0:
  ans = B // A
else:
  ans = B // A + 1
  
print(ans)