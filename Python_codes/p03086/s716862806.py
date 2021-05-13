a = input()
b = ["A","T","G","C"]
c = 0
ans = 0
for i in a:
  if i in b:
    c += 1
    ans = max(ans,c)
  else:
    c = 0
print(ans)