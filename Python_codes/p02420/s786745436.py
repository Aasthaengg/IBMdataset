while True:
    t = input()
    if t == "-":
        break
    n = int(input())
    for i in range(n):
        sn = int(input())
        t = t[sn:]+t[:sn]
    print(t)