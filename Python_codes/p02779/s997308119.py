N=int(input())
A=list(map(int,input().split()))
B=list(dict.fromkeys(A))
if A==B:
    print('YES')
else:
    print('NO')