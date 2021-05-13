N=int(input())
S=0
for i in range(1,N+1):
    S=S+i*(N//i)*(N//i+1)//2
print(S)