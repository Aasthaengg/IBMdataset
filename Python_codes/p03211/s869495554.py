s = input()
a = 1e9
for i in range(len(s)-2):
  a = min(a, abs(753 - int(s[i:i+3])))
print(a)       