x,y = [int(i) for i in input().split()]
ans = 1
for i in range(1,61):
  if y//x < 2**i:
    break
  else:
    ans += 1
print(ans)