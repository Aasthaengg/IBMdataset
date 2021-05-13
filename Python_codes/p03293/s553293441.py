S=list(str(input()))
T=list(str(input()))
for i in range(len(S)):
  if S==T:
    print('Yes')
    exit()
  a=S.pop(-1)
  S.insert(0,a)
print('No')