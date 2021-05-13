def main():
    strA = input()
    listA = strA.split(" ")

    N = int(listA[0])
    R = int(listA[1])

    nRate = 0
    if N >= 10:
        nRate = R
    else:
        nRate = R + (100 * (10 - N))

    print(nRate)

if __name__ == '__main__':
    main()