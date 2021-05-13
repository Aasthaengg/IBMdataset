def resolve():
    X = int(input())
    A = [1]
    for i in range(2, 33):
        for j in range(2, 11):
            tmp = i**j
            if tmp <= X:
                A.append(tmp)
            else:
                break
    print(max(A))


resolve()
