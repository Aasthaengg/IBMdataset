def main():
    # ab = [int(_x) for _x in input().split()]
    K = int(input())
    S = input().strip()
    if (len(S) > K):
        print(S[:K] + "...")
    else:
        print(S)


main()
