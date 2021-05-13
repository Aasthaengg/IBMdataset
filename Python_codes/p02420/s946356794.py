N = input()
while N != "-":
    m = int(input())
    h = 0
    for i in range(m):
        h += int(input())
    h %= len(N)
    t = N[h:len(N)] + N[0:h]
    print(t)
    N = input()
