N, K = map(int,input().split())
S = input()


if K == 1:
  s = S[0].lower() + S[1:]
elif K == N:
  s = S[:-1] + S[-1].lower()
else:
  s = S[:K-1] + S[K-1].lower() + S[K:]

print(s)

