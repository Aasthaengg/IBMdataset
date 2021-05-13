CASES = "abcdefghijklmnopqrstuvwxyz"
s=set(input())
for c in CASES:
  if c not in s:
    print(c)
    exit()
print("None")