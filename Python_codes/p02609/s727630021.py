def popcount(n):
    return bin(n).count('1')


def main():
    N = int(input())
    X = input()

    X_int = int(X, 2)

    pcount_X = popcount(X_int)

    pcount_X_pls1 = pcount_X + 1
    pcount_X_mns1 = pcount_X - 1
    
    X_mod_pcount_X_pls1 = X_int % pcount_X_pls1
    if pcount_X_mns1 != 0:
        X_mod_pcount_X_mns1 = X_int % pcount_X_mns1

    for i,bit in enumerate(X):
        bit = int(bit)
        if bit == 0:
            n = (X_mod_pcount_X_pls1 + pow(2, N-i-1, pcount_X_pls1)) % pcount_X_pls1
        else:
            if pcount_X_mns1 == 0:
                print(0)
                continue
            n = (X_mod_pcount_X_mns1 - pow(2, N-i-1, pcount_X_mns1)) % pcount_X_mns1

        ans = 1
        while n > 0:
            ans += 1
            n %= popcount(n)
        print(ans)
        
main()