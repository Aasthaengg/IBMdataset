N, K = map(int, input().split())
S = input()
tmp = S[K-1]
tmp = chr(ord(tmp)+32)

print(S[:K-1] + tmp + S[K:])
