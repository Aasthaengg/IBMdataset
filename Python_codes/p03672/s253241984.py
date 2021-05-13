S = input()
while True:
    S = S[:-1]
    if len(S)%2 == 0:
        if S[:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            exit(0)