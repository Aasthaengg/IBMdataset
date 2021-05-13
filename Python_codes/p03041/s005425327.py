N,K=list(map(int,input().split()))
S=input()
sdic={"A":"a","B":"b","C":"c"}
print(S[:K-1]+sdic[S[K-1]]+S[K:])