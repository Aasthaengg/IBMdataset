while True:
    a, b = [int(x) for x in input().split()
]
    if a == b == 0:
        break
    print(a, b) if a < b else print(b, a)