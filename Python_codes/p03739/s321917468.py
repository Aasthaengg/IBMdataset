def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    sums = []

    for i in range(n):
        if i == 0:
            sums.append(A[i])
            if A[i] == 0:
                sums[i] = 1
                res += 1
            elif A[i] < 0:
                res += 1 - A[i]
                sums[i] = 1
        else:
            sums.append(sums[i-1] + A[i])
            if sums[i] == 0:
                if sums[i-1] > 0:
                    sums[i] = -1
                    res += 1
                else:
                    sums[i] = 1
                    res += 1
            elif (sums[i-1] > 0) and (sums[i] > 0):
                res += 1 + sums[i]
                sums[i] = -1
            elif (sums[i-1] < 0) and (sums[i] < 0):
                res += 1 - sums[i]
                sums[i] = 1
    
    sums = []
    res1 = 0

    for i in range(n):
        if i == 0:
            sums.append(A[i])
            if A[i] == 0:
                sums[i] = -1
                res1 += 1
            elif A[i] > 0:
                res1 += 1 + A[i]
                sums[i] = -1
        else:
            sums.append(sums[i-1] + A[i])
            if sums[i] == 0:
                if sums[i-1] > 0:
                    sums[i] = -1
                    res1 += 1
                else:
                    sums[i] = 1
                    res1 += 1
            elif (sums[i-1] > 0) and (sums[i] > 0):
                res1 += 1 + sums[i]
                sums[i] = -1
            elif (sums[i-1] < 0) and (sums[i] < 0):
                res1 += 1 - sums[i]
                sums[i] = 1
    
    print(min(res, res1))

if __name__ == '__main__':
    main()