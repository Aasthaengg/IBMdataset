while True:
    T = input()
    if T == '-':
        break
    m = int(input())
    for i in range(m):
        H = int(input())
        T = T[H:] + T[:H]
    print(T)

