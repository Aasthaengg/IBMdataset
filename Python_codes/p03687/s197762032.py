s = list(str(input()))
alpha = [chr(i) for i in range(97, 97+26)]
temp = [[] for _ in range(26)]
k = 0
for i in range(26):
  for j in range(len(s)):
    if alpha[i] == s[j]:
      temp[i].append(j)
M = []      
for i in range(26):
  m = 0
  l = len(temp[i])
  if l != 0:
    m = max([len(s) - temp[i][l - 1] - 1,temp[i][0]])
    for j in range(l-1):
      m = max([m,temp[i][j+1] - temp[i][j]-1])
    M.append(m)
print(min(M))    