while True:
    try: 
        a, b = map(int, input().split())
        cross = a * b

        if a < b:
            a, b = b, a
        while a % b != 0:
            a, b = b, a % b
        print(b, cross // b)
    except EOFError:
        break