import sys
input = sys.stdin.readline


def main():
    T1, T2 = [int(x) for x in input().split()]
    A1, A2 = [int(x) for x in input().split()]
    B1, B2 = [int(x) for x in input().split()]

    if (T1 * A1 + T2 * A2) == (T1 * B1 + T2 * B2):
        print("infinity")
        return


    x = (T1 * A1 + T2 * A2) - (T1 * B1 + T2 * B2)
    y = (T1 * A1) - (T1 * B1)
    if (y > 0 and x > 0) or (y < 0 and x < 0):
        print("0")
        return
    x = abs(x)
    y = abs(y)
    count = (y // x) * 2
    if y % x != 0:
        count += 1
    print(count)






if __name__ == '__main__':
    main()

