N,A,B = map(int,input().split())
mi = A*(N-1)+B
ma = A+B*(N-1)
if (N == 1 and A != B)or ma-mi < 0:
    print(0)
else:
    print(ma-mi+1)