A,B=map(int,input().split())

N=100

S=[[] for _ in range(N)]
for i in range(N):
    if i<N//2:
        S[i]=list("#"*N)
    else:
        S[i]=list("."*N)
        
    
y=0
x=0
for _ in range(A-1):
    S[y][x]="."
    x+=2
    if x>=N:
        x=0
        y+=2
        
y=N//2+1
x=0
for _ in range(B-1):
    S[y][x]="#"
    x+=2
    if x>=N:
        x=0
        y+=2
        
print(N,N)
for i in range(N):
    print(''.join(map(str, S[i])))





