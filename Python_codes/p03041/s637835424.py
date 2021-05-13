N, K = map(int, input().split())
S = list(map(str, input().rstrip()))

S[K-1] = S[K-1].lower()

print(*S, sep="")