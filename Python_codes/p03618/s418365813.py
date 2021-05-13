from collections import defaultdict
dic = defaultdict(int)
S = str(input())
N = len(S)
for i in range(N):
  dic[S[i]] += 1
#print(dic)

ans = 1 #もともと
L = list(dic.keys())
for i in range(len(L)):
  for j in range(i+1,len(L)):
    temp = dic[L[i]]*dic[L[j]]
    ans += temp
print(ans)