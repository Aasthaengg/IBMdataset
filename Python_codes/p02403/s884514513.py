while True:
    data = input()
    if data == '0 0':
        break
    h, w = map(int, data.split())
    print(("#"*w+"\n")*h)