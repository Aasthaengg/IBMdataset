if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7

    numlist = dict()

    if n % 2 == 1:
        for i in range(0, n+1, 2):
            numlist[i] = []
    else:
        for i in range(1, n+1, 2):
            numlist[i] = []

    for aa in a:
        if aa not in numlist.keys():
            print('0')
            exit()
        numlist[aa].append(aa)

    for num in numlist:
        if num == 0 and len(numlist[num]) != 1:
            print('0')
            exit()
        elif num == 0 and len(numlist[num]) == 1:
            continue
        elif len(numlist[num]) != 2:
            print('0')
            exit()

    print(str(pow(2, n//2) % mod))
