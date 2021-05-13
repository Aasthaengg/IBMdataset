H,W,K = map(int,input().split())
S = []
for i in range(H):
  temp = str(input());temp = list(temp)
  S.append(temp)
#print(S)
ans = []
cum = 0
num = 0
for i in range(H):
  if "#" not in S[i]:
    #print(i)
    cum += 1
  else:
    temp = []; num +=1
    First = True
    for j in range(W):
      if S[i][j] == "#":
        if First:
          temp.append(num)
          First = False
        else:
          num +=1
          temp.append(num)
      else:
        temp.append(num)
    ans.append(temp)
    for t in range(cum):
      ans.append(temp)
    cum = 0
if cum > 0:
  for t in range(cum):
    temp = ans[-1]
    ans.append(temp)
for x in ans:
  print(*x)