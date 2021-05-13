N = int(input())
S = str(input())
T = str(input())
ans = S+T
for i in range(min(len(S),len(T))):
  if S[-1-i:] == T[:i+1]:
    ans = S+T[i+1:]

print(len(ans))