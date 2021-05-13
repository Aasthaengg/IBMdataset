while True:
    char = input()
    if char == '-':
        break
    else:
        char = list(char)
        m = int(input())
        for i in range(m):
            sl = int(input())
            a = char[0:sl] #スライス
            b = char.extend(a)#エクステンド
            del char[0:sl] #del
    print("".join(char))

