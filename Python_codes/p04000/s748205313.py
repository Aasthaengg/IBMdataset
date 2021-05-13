H, W, N = list(map(int, input().split()))
ans = {}
for i in range(N):
  a, b = list(map(int, input().split()))
  for j in range(-1, 2):
    for k in range(-1, 2):
      if (a+j)>=2 and (b+k)>=2 and (a+j)<=(H-1) and (b+k)<=(W-1):
        key = str(a+j) + "_" + str(b+k)
        ans[key] = ans.get(key, 0) + 1
ans_value = list(ans.values())
ans_n0 = 0
for i in range(1, 10):
  ans_n0 = ans_n0 + ans_value.count(i)
print((H-2)*(W-2)-ans_n0)
for i in range(1, 10):
  print(ans_value.count(i))
