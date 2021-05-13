K,T = map(int,input().split())
A = list(map(int,input().split()))

MX = max(A)

if K-MX >= MX-1:
    print(0)
else:
    print(2*MX-K-1)
