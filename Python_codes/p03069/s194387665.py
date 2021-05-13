N = int(input())
S = input()

bl, wl = 0, 0
br, wr = S.count('#'), S.count('.')
ret = min(br, wr)
for s in S :
  ret = min(ret, bl + wr)
  if s == '#' :
    bl += 1
    br -= 1
  else :
    wl += 1
    wr -= 1
    
print(ret)