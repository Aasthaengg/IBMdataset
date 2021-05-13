def main():
    MOD = 10 ** 9 + 7
    l = [int(char) for char in input()]

    n = len(l)

    cumsum = []
    tmp = 0
    for number in l:
        if number == 1:
            tmp += 1
        cumsum.append(tmp)
    sel = [pow(2, number, MOD) for number in cumsum]
    sel.append(1)

    def dp(i):
        if l[i] == 0:
            return srs[i-1]
        result = srs[i-1] + sel[i-1] * pow(3, n - 1 - i, MOD)
        result %= MOD
        return result
    
    srs = {-1: 0}
    for i in range(n):
        srs[i] = dp(i)
    
    answer = srs[n-1] + sel[n-1]
    answer %= MOD
    print(answer)


main()
