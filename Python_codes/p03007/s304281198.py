N = int(input())
AA = list(map(int,input().split()))#0を含む可能性あり

A = []
count = 0
for i in range(N):
    if AA[i] != 0:
        A.append(AA[i])
    else:
        count += 1

NN = N - count
B = [abs(A[i]) for i in range(NN)]

if count == 0:
    det = 1
    s = A[0]//B[0]#最初のやつの符号
    for i in range(1,NN):
        if s * A[i] < 0:
            det = -1
            break

    if det == 1:#全て同符号
        m = min(B)

        M = sum(B) - 2 * m
        print(M)

        for i in range(NN):
            if m == B[i]:
                p = i
                break

        C = [A[i]//B[i] for i in range(NN)]

        C[p] *= -1

    else:#異符号が含まれる
        M = sum(B)
        print(M)
        C = [A[i]//B[i] for i in range(NN)]

    fp = -1 #firstplus
    fm = -1 #firstminus
    for i in range(NN):
        if fp == -1 and C[i] == 1:
            fp = i
        elif fm == -1 and C[i] == -1:
            fm = i
        elif fp != -1 and fm != -1:
            break

    X = []
    Y = []

    for i in range(NN):
        if i == fp or i == fm:
            continue
        if C[i] == -1:
            X.append(i)
        else:
            Y.append(i)

    x = A[fp]
    for i in X:
        print(x,A[i])
        x -= A[i]

    y = A[fm]
    for i in Y:
        print(y,A[i])
        y -= A[i]

    print(x,y)

elif A == []:
    print(0)
    for i in range(count-1):
        print(0,0)

else:

    det = 1
    s = A[0]//B[0]#最初のやつの符号
    for i in range(1,NN):
        if s * A[i] < 0:
            det = -1
            break

    M = sum(B)
    print(M)

    if det == 1:#全て同符号
        #これがまずい
        if s < 0:
            for i in range(count-1):
                print(0,0)
            x = 0
            for i in range(NN):
                print(x,A[i])
                x -= A[i]
        else:
            for i in range(count-1):
                print(0,0)
            x = 0
            for i in range(NN-1):
                print(x,A[i])
                x -= A[i]
            print(A[NN-1],x)
            




    else:#異符号が含まれる
        #こちらは今まで通り処理して最後に0を引きまくれば良い
        
        C = [A[i]//B[i] for i in range(NN)]

        fp = -1 #firstplus
        fm = -1 #firstminus
        for i in range(NN):
            if fp == -1 and C[i] == 1:
                fp = i
            elif fm == -1 and C[i] == -1:
                fm = i
            elif fp != -1 and fm != -1:
               break

        X = []
        Y = []

        for i in range(NN):
            if i == fp or i == fm:
                continue
            if C[i] == -1:
                X.append(i)
            else:
                Y.append(i)

        x = A[fp]
        for i in X:
            print(x,A[i])
            x -= A[i]

        y = A[fm]
        for i in Y:
            print(y,A[i])
            y -= A[i]

        print(x,y)

        for i in range(count):
            print(x-y,0)