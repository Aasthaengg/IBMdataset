N = int(input())
S = input()
maxA = 0
for i in range(N):
    maxA = max(maxA, len(set(S[:i]) & set(S[i:])))
print(maxA)
