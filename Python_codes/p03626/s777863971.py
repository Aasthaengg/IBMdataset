N = int(input())
S1 = input()
S2 = input()
ans = 3

for n in range(1,N):
  if S1[n-1]==S2[n-1] or n==1:
    ans*=2
  elif S1[n-1]!=S1[n] and S1[n]!=S2[n]:
    ans*=3

print(ans%(10**9+7))