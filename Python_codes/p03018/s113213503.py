s = list(input())

i = 0
bc = list("BC")

a_cnt = 0
res = 0
i = 0
while i <= len(s)-1:
  if s[i] == "A":
    a_cnt += 1
  elif s[i:i+2] == bc:
    res += a_cnt
    i += 1
  else:
    a_cnt = 0
  i += 1

print(res)