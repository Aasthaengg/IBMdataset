def resolve():
    '''
    code here
    '''
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    res = 0
    for i in range(A+1):
        for j in range(B+1):
            for k in range(C+1):
                if 500*i + 100*j + 50*k == X:
                    res += 1
    print(res)

if __name__ == "__main__":
    resolve()
