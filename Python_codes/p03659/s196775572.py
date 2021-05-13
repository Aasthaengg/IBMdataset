N=int(input())
S=list(map(int,input().split()))
D=[]
goukei=0

for i in range(N):
    goukei+=S[i]
    D.append(goukei)

T=[]    
for i in range(N-1):
    T.append(abs((goukei-D[i])-D[i]))
    
print(min(T))