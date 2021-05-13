while True:
    n = list(map(int, input().split()))
    n.sort()
    if (n[0] == 0 and n[1] == 0):
        break
    else:
        print('{} {}'.format(n[0], n[1]))