s = str(input())
k = int(input())
ch = []
for i in range(1, min(k+1, len(s)+1)):
  for j in range(len(s)-i+1):
    ch.append(s[j:j+i])
ch = list(set(ch))
ch = sorted(ch)
print(ch[k-1])  