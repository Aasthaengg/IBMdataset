def main():

    N = int(input())
    S1 = input()
    S2 = input()

    mod = pow(10, 9) + 7
    i = 0
    count = 1
    isSame = True
    while i < N:
        if S1[i] == S2[i]:
            if isSame:
                if i == 0:
                    count *= 3
                else:
                    count *= 2
            isSame = True
            i += 1
        else:
            if isSame:
                if i == 0:
                    count *= 6
                else:
                    count *= 2
            else:
                count *= 3
            isSame = False
            i += 2
        count %= mod
    return count

if __name__ == '__main__':
    print(main())