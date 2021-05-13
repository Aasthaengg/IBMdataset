def main():
    a, b = list(map(int, input().split()))
    def factorization(num):
        result = set()
        count = 0
        temp = num
        for i in range(2, int(num ** 0.5) + 1):
            if temp % i == 0:
                count = 0
                while temp % i == 0:
                    count += 1
                    temp /= i
                result.add(i)
        if temp != 1:
            result.add(int(temp))
        if result == []:
            result.add(num)
        return result
    print(len(factorization(a) & factorization(b)) + 1)



if __name__ == '__main__':
    main()
