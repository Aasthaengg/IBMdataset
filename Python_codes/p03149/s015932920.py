def main():

    N = list(input().split())
    N.sort()
    if N[0] + N[3] + N[2] + N[1] == "1974":
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())