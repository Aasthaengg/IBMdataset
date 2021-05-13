D = int(input())
c = list(map(int,input().split()))
S = []
for _ in range(D):
  line = list(map(int,input().split()))
  S.append(line)
T = []
for _ in range(D):
  t = int(input())
  T.append(t)
dic = {n+1:0 for n in range(26)}
ans = 0
for i in range(1,D+1):
  dic[T[i-1]] = i
  ans += S[i-1][T[i-1]-1]
  for j in range(26):
    ans -= c[j]*(i - dic[j+1])
  print(ans)