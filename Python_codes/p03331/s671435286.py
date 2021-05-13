N=int(input())

ans=[]

for i in range(1,N):
    B=N-i
    ans.append(sum(map(int,str(i)))+sum(map(int,str(B))))

print(min(ans))