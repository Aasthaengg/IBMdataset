N=int(input())
ans=100000000000
for A in range(1,N):
    B=N-A
    sa=0
    sb=0
    for i in range(len(str(A))):
        sa+=A%10
        A=(A-A%10)//10
    for j in range(len(str(B))):
        sb+=B%10
        B=(B-B%10)//10
    if sa+sb<ans:
        ans=sa+sb

print(ans)
