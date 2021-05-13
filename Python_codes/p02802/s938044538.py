n,m = map(int,input().split())

flag = dict()
for i in range(m):
  q, s = input().split()
  if q not in flag:
    flag[q] = [0,0]
    if s == "AC":
      flag[q][0] += 1
    else:
      flag[q][1] += 1
  else:
    if flag[q][0] != 1:
      if s == "AC":
        flag[q][0] += 1
      else:
        flag[q][1] += 1
      
ans = [0,0]
for v in flag.values():
  if v[0]:
    ans[0] += 1
    ans[1] += v[1]

print(ans[0],ans[1])
