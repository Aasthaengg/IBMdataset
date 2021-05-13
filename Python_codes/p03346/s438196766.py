n = int(input())
p = [int(input()) for i in range(n)]
q = [0] * n
now = 1
for k,v in enumerate(p):
  q[v-1] = k
now = -1
ans = 1
mini_ans = 0
for i in q:
  if i > now:
    mini_ans += 1
  else:
    ans = max(ans,mini_ans)
    mini_ans = 1
  now = i
ans = max(ans,mini_ans)
ans = n-ans
print(ans)