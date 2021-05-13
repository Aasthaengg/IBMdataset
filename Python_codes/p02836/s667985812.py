S = input()

leng = len(S)
count = 0
if leng % 2 == 0:
  S1 = S[:int(leng/2)]
  S2 = S[int(leng/2):]
  for i in range(int(leng/2)):
    if S1[i] == S2[int(leng/2)-1-i]:
      count += 1
  print(int(leng/2)-count)
else:
  S1 = S[:int(leng/2)]
  S2 = S[int(leng/2)+1:]
  for i in range(int(leng/2)):
    if S1[i] == S2[int(leng/2)-1-i]:
      count += 1
  print(int(leng/2)-count)
