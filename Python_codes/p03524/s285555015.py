s = input()
a = {"a":0, "b":0, "c":0}
for i in s:
  a[i] += 1
if max(a.values()) - min(a.values()) <= 1:
  print("YES")
else:
  print("NO")