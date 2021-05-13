while True:
    s = input()
    if s==('-'):
        break
    m = int(input())
    S=s
    for i in range(m):
        h = int(input())
        S = S[h:len(s)] + S[0:h]
    print(S)
