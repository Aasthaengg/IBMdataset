n,k = map(int,input().split())
S = list(input())
S[k-1] = S[k-1].lower()
print("".join(S))
