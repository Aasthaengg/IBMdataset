# AOJ ITP1_7_D

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    a = numinput()
    n = a[0]; m = a[1]; l = a[2]
    A = []; B = []; C = []

    for i in range(n):
        A.append(numinput())
    for j in range(m):
        B.append(numinput())

    for i in range(n):
        list = []
        for k in range(l):
            sum = 0
            for j in range(m):
                sum += A[i][j] * B[j][k]
            list.append(sum)
        C.append(list)

    for i in range(n):
        _str_ = ""
        for k in range(l - 1):
            _str_ += str(C[i][k]) + " "
        _str_ += str(C[i][l - 1])
        print(_str_)

if __name__ == "__main__":
    main()
