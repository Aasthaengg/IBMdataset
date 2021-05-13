from itertools import product
def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    for a in A:
        if a[2] > 0:
            t = a
            break
    for x, y in product(range(0, 101), repeat = 2):
        H = t[2] + abs(t[0] - x) + abs(t[1] - y)
        for a in A:
            if a[2] == 0 and H > abs(a[0] - x) + abs(a[1] - y):
                break
            elif a[2] != 0 and a[2] != H - abs(a[0] - x) - abs(a[1] - y):
                break
        else:
            ansx, ansy = x, y
            break
    H = t[2] + abs(t[0] - ansx) + abs(t[1] - ansy)
    print('{} {} {}'.format(ansx, ansy, H))

if __name__ == '__main__':
    main()
