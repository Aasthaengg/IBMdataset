N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
U=[]
for i in range(N):
    U.append(abs(A-(T-0.006*H[i])))
for i in range(N):
    if U[i]==min(U):
        print(i+1)
        break