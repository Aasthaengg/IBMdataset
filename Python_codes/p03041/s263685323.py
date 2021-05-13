N, K = map(int, input().split())
S = list(str(input()))

S[K-1] = S[K-1].lower()

print("".join(S), end='')