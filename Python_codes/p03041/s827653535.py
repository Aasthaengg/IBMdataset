N,K=map(int,input().split())
S=input()
s=S[:K-1]
s+=S[K-1].swapcase()
s+=S[K:]
print(s)