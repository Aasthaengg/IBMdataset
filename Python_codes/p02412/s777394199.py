while True:
    i = 0
    n,x = map(int,raw_input().split())
    if n == x == 0:
        break
    for a in range(1,n+1):
        for b in range(1,a+1):
            for c in range(1,b+1):
                if not a == b == c and not a == b and not a == c and not b == c:
                    if a+b+c == x:
                        i = i + 1
    print i