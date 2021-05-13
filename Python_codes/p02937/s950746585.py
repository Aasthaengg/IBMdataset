from sys import exit

s = input()
t = input()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alph_list = dict()
for i in range(26):
  alph_list[alphabet[i]] = i

counter = [[] for _ in range(26)]

for i in range(len(s)):
  key = s[i]
  counter[alph_list[key]].append(i)

ans = 0
ans_mod = 0
flag = True
for i in range(len(t)):
  key = alph_list[t[i]]
  if not counter[key]:
    flag = False
    break
  l, r = 0, len(counter[key])
  while r-l > 1:
    bit = (r+l)//2
    if counter[key][bit] >= ans:
      r = bit
    else:
      l = bit
  if r == len(counter[key]) and counter[key][l] < ans:
    ans_mod += 1
    ans = counter[key][0]+1
  elif l == 0 and counter[key][l] >= ans:
    ans = counter[key][l]+1
  else:
    ans = counter[key][r]+1
if flag:
  print(ans_mod*len(s)+ans)
else:
  print(-1)