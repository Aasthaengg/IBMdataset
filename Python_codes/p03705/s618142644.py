N,A,B = [int(i) for i in input().split()]

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    exit()

if A > B:
    print(0)
    exit()

print((A+(N-1)*B)-((N-1)*A+B)+1)
