def main():
    # ab = [int(_x) for _x in input().split()]
    N = int(input())
    nn = N % 10
    if nn == 3:
        print("bon")
    elif nn in [0, 1, 6, 8]:
        print("pon")
    else:
        print("hon")


main()
