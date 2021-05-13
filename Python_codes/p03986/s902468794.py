x = input()

s, t = 0, 0
ols = 0
cnt = 0
for i in x:
  if i == "S":
    s += 1
  else:
    if s > 0:
     cnt += 1
     s -= 1
     s = max(s,0)
print (len(x)-cnt*2)