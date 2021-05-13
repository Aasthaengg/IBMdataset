from collections import Counter

w=input()

d=Counter(w)

ans="Yes"

for i in d.values():
  if i%2!=0:
    ans="No"
    break

print(ans)