def resolve():
    Sd = list(input())
    T = input()
    res = ""
    for i in range(len(Sd)):
        for j in range(len(T)):
            if i + j >= len(Sd):
                break
            if Sd[i + j] != "?" and Sd[i + j] != T[j]:
                break
        else:
            tmp = "".join(Sd[:i]) + T + "".join(Sd[i + len(T):])
            if res == "":
                res = tmp
            else:
                if res > tmp:
                    res = tmp
    if res == "":
        print("UNRESTORABLE")
        return
    for s in res:
        if s == "?":
            s = "a"
        print(s, end="")
    print()

resolve()
