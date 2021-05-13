import string
al = string.ascii_lowercase

S = set(input())

for i in al:
  if i not in S:
    print(i)
    exit()

print("None")