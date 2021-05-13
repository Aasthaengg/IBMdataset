N = int(input())
S1 = list(input())
S2 = list(input())

if len(S1) == 1:
    print(3)
elif len(S1) == 2:
    print(6)
else:
    if S1[0] != S2[0]:
        t = 2
        i = 2
        a = 6
    else:
        t = 1
        i = 1
        a = 3
    while True:
        if S1[i] != S2[i]:
            if t == 2:
                a *= 3
            else:
                a *= 2
            i += 2
            t = 2
        else:
            if t == 2:
                a *= 1
            else:
                a *= 2
            i += 1
            t = 1
        a %= 1000000007
        if i == len(S1):
            print(a)
            break
