def main():
    h, w = map(int, input().split())
    c = list(list(input()) for i in range(h))

    for i in range(2*h):
        for j in range(w):
            print(c[int(i/2)][j], end='')
        print()

main()
