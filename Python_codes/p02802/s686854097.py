n,m = map(int, input().split())

flag = [False]*n
nums = [0]*n
for _ in range(m):
  p,s = input().split()
  p = int(p)-1
  if s == "AC": flag[p] = True
  elif flag[p] == False: nums[p] += 1
ac = flag.count(True)
wa = 0
for i in range(n):
  if flag[i]: wa += nums[i]
print(ac, wa)