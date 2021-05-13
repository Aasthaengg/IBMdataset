A,B,K = map(int,input().split())

if K >= A:
    B -= K-A
    A = 0

else:
    A -= K

if A <= 0 and B <= 0:
    print(0,0)
else:
    print(A,B)
