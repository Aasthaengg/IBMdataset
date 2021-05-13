def main():
    S = input()
    mod = pow(10, 9) + 7
    n = len(S)
    # print(S)
    countA, countAB, countABC = 0, 0, 0
    strA, strNonA = 0, 1
    for i in range(n):
        if S[i] == "A":
            countA += strNonA + strA
            strA += strNonA
            strNonA = 0
        elif S[i] == "B":
            countAB += countA
        elif S[i] == "C":
            countABC += countAB
        else:
            countABC = 3*countABC + countAB
            countAB = 3*countAB + countA
            countA = 3*countA + strNonA + strA
            strA = 3*strA + strNonA
            strNonA *= 2

        countA %= mod
        countAB %= mod
        countABC %= mod
        strA %= mod
        strNonA %= mod
        # print(countA, countAB, countABC, strA, strNonA)

    return countABC % mod

if __name__ == '__main__':
    print(main())