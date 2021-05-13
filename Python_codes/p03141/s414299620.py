N=int(input())
AB=[list(map(int,input().split()))+[i] for i in range(N)]
A=sorted(AB,key=lambda x:x[1]+x[0],reverse=True)
value=0
for i in range(N):
    if i%2==0:
        value+=A[i][0]
    else:
        value-=A[i][1]
print(value)
