N,A,B=input().split()
N=int(N)
A=int(A)
B=int(B)

total=0
for i in range(N+1):
    N_str=str(i)
    N_sum=sum(list(map(int,N_str)))
    if N_sum<=B and N_sum>=A:
        total+=i
print(total)