s = input()
N = len(s)
pc = 0
gc = 0
wp = 0
lp = 0
for i in range(N):
  if s[i] == "g":
    if pc+1 <= gc:
      pc += 1
      wp += 1
    else:
      gc += 1  
  if s[i] == "p":  
    if pc+1 <= gc:
      pc += 1
    else:
      gc += 1  
      lp += 1
print(wp-lp)      