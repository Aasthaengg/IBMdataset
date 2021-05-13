N, K = map(int,input().split())
S = input()
a = S[:K-1] + str.lower(S[K-1]) + S[K:]
print(a)