N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')
ans = r*g*b

for i in range(N):
  for j in range(i+1,N):
    k=2*j-i
    if k<N and S[i]!=S[j]!=S[k]!=S[i]:
      ans -= 1

print(ans)