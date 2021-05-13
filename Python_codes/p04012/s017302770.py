def resolve():
    w = input()
    flag = 0
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(abc)):
        if w.count(abc[i])%2 == 0:
            continue
        else:
            flag = 1
    print("Yes" if flag == 0 else "No")
resolve()