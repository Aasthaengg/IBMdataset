N = int(input())
S = input()

table = [0] * (len(S)+1)
wordDict = {}

for i in range(len(S)):
  if S[i] in wordDict :
    wordDict[S[i]] = [wordDict[S[i]][0], i]
  else:
    wordDict[S[i]] = [i+1, i]

for ran in wordDict.values():
  if ran[0] > ran[1]:
    continue
  for i in range(ran[0], ran[1]+1):
    table[i] += 1

maxNum = 0
for i in range(len(S)+1):
  maxNum = max(maxNum, table[i])

print(maxNum)
  


