Row = int(input())
dictA= {}
a = ""
mid = 0
for i in range (Row):
  a = input()
  dictA.setdefault(a,0) 
  dictA[a] += 1
  mid = max(mid, dictA[a])
sDict = sorted(dictA.items())
for i in range(len(dictA)):
  if sDict[i][1]== mid:
    print(sDict[i][0])