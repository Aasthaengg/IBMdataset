#"a" 97 "z" 122
s = list(ord(i) for i in input())
k = int(input())

for i in range(len(s)-1):
  if s[i] == ord("a"): continue
  t = ord("z")+1-s[i]
  if k >= t:
    s[i] = 97
    k -= t
if k > 0:
  k %= 26
  s[-1] += k
  if s[-1] > ord("z"):
    s[-1] -= 26
print("".join(list(map(chr, s))))