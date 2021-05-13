N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
ans=sum(A)
if N<ans:
    print('-1')
else:
    print(N-ans)
