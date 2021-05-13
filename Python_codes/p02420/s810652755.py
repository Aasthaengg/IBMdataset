while True:
    try:
        card = list(str(input()))
        if card[0] == '-':
            break
        m = int(input())
        h = [0]*m
        for i in range(m):
            h[i] = int(input())
        for i in range(len(h)):
            tmp = card[0:h[i]]
            card = card[h[i]:]+tmp

        for i in range(len(card)-1):
            print(card[i],end = '')
        print(card[-1])
    except EOFError:
        break