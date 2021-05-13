def math(A,B):
    if B%A ==0:
        print(A+B)
    else:
        print(B-A)
A,B = tuple(map(int, input().split()))

math(A,B)