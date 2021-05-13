N = int(input())
S = list(input())
sumi, result = [], 0
while len(sumi)<10 and N>0:
  x = S.pop(0)
  N -= 1
  if x in sumi:
    continue
  sumi.append(x)
  sumi_2, i = [], 0
  for i in range(N-1):
      s = S[i]
      if s in sumi_2:
        continue
      sumi_2.append(s)
      result += len(set(S[i+1:]))
print(result)