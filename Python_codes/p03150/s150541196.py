S = input()


def f():
    for i in range(len(S)):
        for j in range(len(S)):
            if S[:i] + S[j:] == "keyence":
                print("YES")
                return
    else:
        print("NO")


f()
