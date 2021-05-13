N = int(input())
S = input()
ans = max(len(set(S[i:]) & set(S[:i])) for i in range(1, N))
print(ans)
