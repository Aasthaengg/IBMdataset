def resolve():
    S = int(input())
    if S%2 == 0:
        print(S//2-1)
    else:
        print((S-1)//2)
resolve()