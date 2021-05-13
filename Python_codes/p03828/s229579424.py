from collections import defaultdict
def main():
    def factorization(num):
        result = []
        count = 0
        temp = num
        for i in range(2, int(num ** 0.5) + 1):
            if temp % i == 0:
                count = 0
                while temp % i == 0:
                    count += 1
                    temp /= i
                result.append([i, count])
        if temp != 1:
            result.append([int(temp), 1])
        if result == []:
            result.append([num, 1])
        return result
    n = int(input())
    d = defaultdict(int)
    mod = 1000000007
    if n == 1:
        print(1)
        exit()
    for i in range(2, n + 1):
        res = factorization(i)
        for (f, v) in res:
            d[f] += v
    ans = 1
    for v in d.values():
        ans = ans * (v + 1) % mod
    print(ans)



if __name__ == '__main__':
    main()
