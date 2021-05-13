r, D, x = list(map(lambda a: int(a), input().split(" ")))
 
ans = []
for i in range(10):
  x = r * x - D
  ans.append(str(x))
 
print("\n".join(ans))