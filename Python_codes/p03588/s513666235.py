N=int(input())
U=[]
for i in range(N):
    A=list(map(int,input().split()))
    U.append(A)

U.sort(reverse=True)
print(U[0][0]+U[0][1])