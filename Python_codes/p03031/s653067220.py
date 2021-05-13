N,M=map(int,input().split())
k=[list(map(int,input().split())) for _ in range(M)] 
*p,=map(int,input().split())
print(sum(1for i in range(2**N) if M==sum(1for j in range(M) if sum(1for h in k[j][1:] if i>>(h-1)&1)%2==p[j])))