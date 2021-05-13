def resolve():
    X, Y = list(map(int, input().split(" ")))
    A = [X]
    while Y >= A[-1]*2:
        A.append(A[-1]*2)
    print(len(A))



if '__main__' == __name__:
    resolve()