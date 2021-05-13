import collections

N = int(input())
S=[]
for i in range(N):
  S.append(input())
ans=collections.Counter(S)
print(len(ans.keys()))