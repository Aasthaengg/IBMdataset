N,K=map(int,input().split())
S=list(input())
S[K-1]='a' if S[K-1]=='A' else ('b' if S[K-1]=='B' else 'c')
print(''.join(S))