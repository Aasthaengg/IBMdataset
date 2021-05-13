A = input()
B = input()

if len(A) > len(B):
    print("GREATER")
elif len(A) < len(B):
    print("LESS")
else:
    i = 0
    while True:
        if A[i] > B[i]:
            print("GREATER")
            break
        elif A[i] < B[i]:
            print("LESS")
            break
        else:
            if i == len(A)-1:
                print("EQUAL")
                break
            else:
                i += 1