N,K = map(int,input().split())
dic = {"A":"a","B":"b","C":"c"}
S = list(input())
S[K-1]=dic[S[K-1]]
print("".join(S))