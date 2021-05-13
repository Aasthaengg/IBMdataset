sd = input()
t = input()
ls = len(sd)
lt = len(t)
ans=[]
for i in range(ls-lt,-1,-1):
  for j, k in zip(sd[i:i+lt], t):
    if j != "?" and j != k:
      break
  else:
    temp = sd[:i] + t + sd[i+lt:]
    ans.append(temp.replace("?","a"))

if not ans:
  print("UNRESTORABLE")
else:
  ans.sort()
  print(ans[0])