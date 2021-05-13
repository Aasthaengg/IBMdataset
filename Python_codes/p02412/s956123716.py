while True:
    try:
        n,x = map(int,input().split(" "))
        if n == 0 and x == 0:
            break
        pattern = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for h in range(j+1,n+1):
                    if i + j + h == x:
                        pattern += 1
        print(pattern)
    except (EOFError):
        break