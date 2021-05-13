import copy
char = list(map(chr, range(ord('a'), ord('z')+1)))
target = list(input())
ans = float("inf")
for c in char:
  s = copy.deepcopy(target)
  tmpans = 0
  while True:
    flag = True
    for si in s:
      if si != s[0]:
        flag = False
    if flag==True:
      break
    for i in range(len(s)-1):
      if s[i] == c or s[i+1] == c:
        s[i] = c
    s.pop()
    tmpans += 1
  if ans > tmpans:
    ans = tmpans
print(ans)
     

