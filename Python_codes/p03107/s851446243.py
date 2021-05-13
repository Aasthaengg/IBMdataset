S = input()
bl = 0
re = 0
for i in S:
  if i == "0":
    re += 1
  else:
    bl += 1
print(min(bl,re)*2)