N=int(input())
for i in range(N):
    a,b,c=map(int,input().split())
    A=a**2
    B=b**2
    C=c**2
    if A+B==C:print('YES')
    elif A+C==B:print('YES')
    elif B+C==A:print('YES')
    else:print('NO')