import math
import itertools

def combination_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main():
    N = int(input())    # maximum of N is 10^5

    for i in range(2, 500):
        tmp = combination_count(i, 2)
        if N < tmp:
            print('No')
            return
        elif N == tmp:
            print('Yes')
            array = [x+1 for x in range(i)]
            accum = [[] for x in range(i)]
            for idx, (i, j) in enumerate(itertools.combinations(array, 2)):
                accum[i-1].append(idx + 1)
                accum[j-1].append(idx + 1)
            print(len(accum))
            for item in accum:
                txt = str(len(item)) + " " + " ".join([str(x) for x in item])
                print(txt)
            return
        else:
            continue

    return


main()