N,X,T=map(int,input().split())
kai=int(N/X)
if N%X==0:
    kot=kai*T
else:
    kot=(kai+1)*T
print(kot)