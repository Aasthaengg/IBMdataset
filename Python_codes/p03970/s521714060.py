s = input()
r = "CODEFESTIVAL2016"

ans = 0

for si, ri in zip(s,r):
  if si != ri:
    ans += 1
    
print(ans)