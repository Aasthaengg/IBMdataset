a = list(map(int,input().split()))
A=a[0]
B=a[1]
C=a[2]

if A==B and B==C and C==A:
    print('Yes')
else:
    print('No')
