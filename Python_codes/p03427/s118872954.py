n = input()

s = 0
for each in n:
  s += int(each)

l = int(n[0]) -1 + 9*(len(n)-1)

print(max(s, l))