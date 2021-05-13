if __name__ == '__main__':
    s = input()
    N = len(s)
    res = 0
    for bit in range(1 << N - 1):
        tmp = 0
        for i in range(N - 1):
            tmp *= 10
            tmp += int(s[i])
            if bit & (1 << i):
                res += tmp
                tmp = 0
        tmp *= 10
        tmp += int(s[-1])
        res += tmp
    
    print(res)