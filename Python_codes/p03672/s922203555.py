S = input()
maxS = ""
for i in range(len(S)//2):
  tmp = S[:i]*2
  j = 2*i
  if tmp == S[:j]:
    maxS = tmp
print(len(maxS))