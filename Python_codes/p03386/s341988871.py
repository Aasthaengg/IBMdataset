A,B,K=map(int,input().split())
s=[]
for i in range(K):
  s.append(A+i)
  s.append(B-i)
s=sorted(list(set(s)))
for j in range(len(s)):
  if A<=s[j] and s[j]<=B:
    print(s[j])