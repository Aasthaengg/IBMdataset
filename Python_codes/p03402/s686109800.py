import sys

input = sys.stdin.readline


def main():
    A, B = [int(x) for x in input().split()]

    C = []
    for i in range(100):
        if i < 50:
            C.append(["#"] * 100)
        else:
            C.append(["."] * 100)

    whitecnt = 1
    blackcnt = 1

    for i in range(1, 50, 2):
        if whitecnt == A:
            break
        for j in range(1, 100, 2):
            C[i][j] = '.'
            whitecnt += 1
            if whitecnt == A:
                break
    for i in range(51, 100, 2):
        if blackcnt == B:
            break
        for j in range(1, 100, 2):
            C[i][j] = '#'
            blackcnt += 1
            if blackcnt == B:
                break

    print(100, 100)
    for c in C:
        print("".join(c))




if __name__ == '__main__':
    main()
