A, B = list(map(int,input().split()))

if A == B:
    print(A*2)
elif (A == B + 1) or (A + 1 == B):
    print(A+B)
else:
    print(max(A+(A-1), B+(B-1)))