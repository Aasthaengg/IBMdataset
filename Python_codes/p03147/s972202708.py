N = int(input())
A = list(map(int, input().split())) + [0]
ans = 0
for h in range(1, 101):
  flag = False
  for a in A:
    if a >= h:
      flag = True
    elif flag:
      ans += 1
      flag = False
print(ans)