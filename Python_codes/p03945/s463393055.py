S = input()
count = 0
p = ''
for s in S:
  if s != p:
    p = s
    count += 1
print(count-1)