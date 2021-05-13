def dotes(S,K):
    if K== len(S) or len(S)<K:
        return S
    else:
        S=S[:K]
        S=S+'...'
        return S
K=int(input())
S=input()
print(dotes(S,K))