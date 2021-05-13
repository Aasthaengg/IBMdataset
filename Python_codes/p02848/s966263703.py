n = int(input())
s = list(map(ord, list(input())))
for i in range(len(s)):
  s[i] += n
  if s[i] > ord('Z'): s[i] -= 26
print("".join(map(chr,s)))