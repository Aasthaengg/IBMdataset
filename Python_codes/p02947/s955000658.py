from collections import Counter

N = int(input())

lst = []

for _ in range(N):
  S = input()
  S = sorted(S)
  S = ''.join(S)
  lst.append(S)

dic = Counter(lst)

rlt = 0
for k in dic:
  rlt += (dic[k]-1)*dic[k]//2
  
print(rlt)