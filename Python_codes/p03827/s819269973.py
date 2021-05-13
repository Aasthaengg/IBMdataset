n = int(input())
s = list(input())
ans,box = 0,[]
box.append(ans)
for i in range(n):
  if s[i] == "I":
    ans += 1
  else:
    ans -= 1
  box.append(ans)
print(max(box))