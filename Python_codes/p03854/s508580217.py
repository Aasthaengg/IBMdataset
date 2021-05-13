S = list(input())
N = len(S)

def f(x):
    print(x)
    exit()

if N < 5:
    f("NO")
elif S[0] == "d":
    w = 1
elif S[0] == "e":
    w = -1
else:
    f("NO")

i = 0
while True:
    if w > 0:
        if S[i]+S[i+1]+S[i+2]+S[i+3]+S[i+4] == "dream":
            i += 5
            if i == N:
                f("YES")
            elif S[i] == "d":
                pass
            elif S[i] == "e":
                if i+1 <= N-1:
                    if S[i+1] == "r":
                        if i+1 == N-1:
                            f("YES")
                        elif S[i+2] == "a":
                            w *= -1
                        elif S[i+2] == "e":
                            i += 2
                            w *= -1
                        elif S[i+2] == "d":
                            i += 2
                        else:
                            f("NO")
                    else:
                        f("NO")
                else:
                    f("NO")
            else:
                f("NO")
        else:
            f("NO")
    elif w < 0:
        if S[i]+S[i+1]+S[i+2]+S[i+3]+S[i+4] == "erase":
            i += 5
            if i == N:
                f("YES")
            if S[i] == "r":
                i += 1
                if i == N:
                    f("YES")
            if S[i] == "d":
                w *= -1
            elif S[i] == "e":
                pass
            else:
                f("NO")
        else:
            f("NO")
    if i+4 > N-1:
        f("NO")
