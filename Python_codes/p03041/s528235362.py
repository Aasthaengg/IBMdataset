N,K=map(int,input().split())
S=input()
S = S[:K-1] + chr(ord(S[K-1])+32) + S[K:]
print(S)