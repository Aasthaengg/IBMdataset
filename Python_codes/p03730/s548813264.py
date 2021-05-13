def resolve():
    a,b,c = map(int, input().split())
    a %= b
    OK = False
    for i in range(b):
        if (a * i)%b == c:
            OK = True
    print("YES") if OK else print("NO")

resolve()