A=list(map(int,input().split()))
S=input()
K=A[1]
s=S[K-1]
s=s.lower()
print(S[:K-1]+s+S[K:])