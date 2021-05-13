N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
h=abs(A-(T-(H[0]*0.006)))
m=1
for i in range(1,N):
    if h>abs(A-(T-(H[i]*0.006))):
        h=abs(A-(T-(H[i]*0.006)))
        m=i+1
print(m)