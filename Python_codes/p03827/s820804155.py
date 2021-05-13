def resolve():
    N = input()
    S = input()
    x = 0
    max_x = 0
    for i in range(len(S)):
        if S[i] == "I":
            x += 1
            if x > max_x:
                max_x = x
        elif S[i] == "D":
            x -= 1
    print(max_x)

resolve()