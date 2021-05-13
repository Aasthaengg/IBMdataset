N,K = map(int,input().split())
S = list(input())

x = S[K-1]
S[K-1] = x.lower()

print("".join(S))