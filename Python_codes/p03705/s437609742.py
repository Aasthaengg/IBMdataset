def resolve():
    '''
    code here
    '''
    N, A, B = [int(item) for item in input().split()]

    if A <= B:
        if N >=3:
            res = (N-1)*B + A - ((N-1)*A + B) + 1

        elif N == 2:
            res = 1
        else:
            if A == B:
                res = 1
            else:
                res = 0
    else:
        res = 0

    print(res)

if __name__ == "__main__":
    resolve()
