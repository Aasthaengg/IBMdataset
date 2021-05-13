while True:
    s = input()
    if s == "-":
        break
    N = int(input())
    for i in range(N):
        H = int(input())
        s = s[H:] + s[:H]
    print(s)
