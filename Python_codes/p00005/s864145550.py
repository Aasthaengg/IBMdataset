while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    ab = a*b
    while b:
        a, b = b, a%b
    print(a, ab//a)