from sys import setrecursionlimit

setrecursionlimit(10 ** 8)

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

    def dp(i, _cache={-1: 0}):
        if i in _cache:
            return _cache[i]
        if l[i] == 0:
            result = dp(i-1)
            _cache[i] = result
            return result
        result = dp(i-1) + sel[i-1] * pow(3, n - 1 - i, MOD)
        result %= MOD
        _cache[i] = result
        return result
    
    answer = dp(n-1) + sel[n-1]
    answer %= MOD
    print(answer)


main()
