N,K=map(int,input().split())
S=input()
S2=S.lower()
S3=''

for i in range(N):
  if i==K-1:
    S3+=S2[i]
  else:
    S3+=S[i]
    
print(S3)