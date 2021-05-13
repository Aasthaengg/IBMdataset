K,A,B  = map(int, input().split())
n = (K-A+1)//2
if B-A < 2:
    print(1+K)
else:
    if (K-A+1)%2 == 0:
        print(A+(B-A)*n)
    else:
        print(A+(B-A)*n+1)