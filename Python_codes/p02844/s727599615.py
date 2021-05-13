N = int(input())
S = input()
ans = 0
for i in range(1000):
  p = str(i).zfill(3)
  if S.find(p[0])==-1:
    continue
  S1 = S[S.find(p[0])+1:]
  if S1.find(p[1])==-1:
    continue
  S2 = S1[S1.find(p[1])+1:]
  if S2.find(p[2])==-1:
    continue
  ans+=1
print(ans)