N, K = map(int, input().split())
S = list(str(input()))

S[K-1] = chr(ord(S[K-1]) + 32)
S = "".join(S)
print(S)