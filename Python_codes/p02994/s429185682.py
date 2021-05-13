N,L=map(int,input().split())

tot=N*L+(N-1)*N/2
ans=[]


for i in range(N):
    ans.append(abs(L+i))

a=ans.index(min(ans))

print(int(tot-(a+L)))
