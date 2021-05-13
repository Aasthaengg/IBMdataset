S = str(input())
N = len(S)
L = list(S)
L = set(L)
if N != 26: #含まないものがある
  for i in range(26):
    temp = chr(i+97)
    if temp not in L:
      ans = S+temp
      print(ans)
      exit()
M = []
All = [chr(97+i) for i in range(26)]
#print(All)
for i in range(25):
  now = 25-i
  M.append(S[now])
  if S[now] > S[now-1]:
    M.sort()
    for x in M:
      if x > S[now-1]:
        temp = x
        ans = S[:now-1]+temp
        print(ans)
        exit()
  
print(-1)  