s = input()
n = len(s)

for start in range(n):
  for end in range(start, n):
    tmp_s = s[:start] + s[end:]
    if tmp_s == "keyence":
      print("YES")
      exit(0)

print("NO")
