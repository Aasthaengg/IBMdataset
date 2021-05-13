s = input()
tmp = 0
max = 0
def check(i):
  if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
    return True
  else:
    return False
for i in range(len(s)):
  if check(i):
    tmp += 1
  else:
    tmp = 0
  if tmp > max:
    max = tmp
print(max)