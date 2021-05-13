N=int(input())
*A,=map(int,input().split())

t=sum([i for i in A if i%2!=0])%2
print('YES' if t==0 else 'NO')