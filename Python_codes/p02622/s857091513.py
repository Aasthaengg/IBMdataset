s = input()
t = input()

s_len = len(s)
count = 0
for i in range(s_len):
  if s[i] !=  t[i]:
    count += 1
print(count)