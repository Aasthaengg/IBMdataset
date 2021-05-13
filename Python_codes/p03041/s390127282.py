N, K = map(int, input().split())
S = input()
print(S[:K-1] + chr(ord(S[K-1]) - ord('A') + ord('a')) +S[K:])