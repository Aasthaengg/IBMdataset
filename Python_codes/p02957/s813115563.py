A,B = map(int,input().split())
if A>B:
    A,B = B,A
if (B-A)%2==0:
    print((B+A)//2)
else:
    print("IMPOSSIBLE")