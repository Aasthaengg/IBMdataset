s = input()
ans = [0,0]
for v in s:
  if v == "C": ans[0] = 1
  elif v =="F" and ans[0] == 1:
    ans[1] = 1
print("Yes" if sum(ans)==2 else "No")