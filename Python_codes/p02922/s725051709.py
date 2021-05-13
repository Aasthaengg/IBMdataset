n = [int(i) for i in input().split()]
m = 1
ans = 0
while m < n[1]:
  ans += 1
  m += n[0]-1
print(ans)