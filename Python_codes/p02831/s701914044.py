A,B=map(int,input().split())
if B > A:
    A,B = B,A

for i in range(1, B+1):
    if (A * i) % B == 0:
        print(A * i)
        break