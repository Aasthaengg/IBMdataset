n = int(input())
d = list(map(int,input().split()))
cnt = {}
for i in d:
  if i not in cnt:
    cnt[i] = 1
  else:
    cnt[i] += 1
m = int(input())
t = list(map(int,input().split()))
flag = True
for i in t:
  if i in cnt:
    if cnt[i]>0:
      cnt[i] -= 1
    else:
      flag = False
      break
  else:
    flag = False
    break
if flag:
  print("YES")
else:
  print("NO")
