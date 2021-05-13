from math import gcd
from functools import reduce
def main():
    N = int(input())
    A = list(map(int, input().split()))

    M = 10**6+1
    mp = [0]*M
    for a in A:
        mp[a] += 1

    pairwise = 1
    for i in range(2,M):
        if sum(mp[i::i])>1:
            pairwise = 0
            break

    if pairwise:
        print('pairwise coprime')
    elif reduce(gcd, A) == 1:
        print('setwise coprime')
    else:
        print('not coprime')

if __name__ == '__main__':
    main()
