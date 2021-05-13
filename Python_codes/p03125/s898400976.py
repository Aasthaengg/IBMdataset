A,B = tuple(map(int,input().split()))
if int(int(B/A)*A) == B:
    print(A+B)
else:
    print(B-A)