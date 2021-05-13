while True:
    N = input()
    if N =='-':
        break
    N = list(N)
    m = int(input())
    for i in range(m):
        h = int(input())
        t = N[0:h]
        del N[0:h]
        N.extend(t)
    print(''.join(N))
