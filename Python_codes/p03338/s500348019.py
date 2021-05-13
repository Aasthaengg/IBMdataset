n = int(input())
s = list(input())
box = []
for i in range(1,n):
  l,r = s[:i],s[i:]
  total = set(l) & set(r)
  box.append(len(total))
print(max(box))