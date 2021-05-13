def main():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n//i)
        divisors.sort(reverse = True)
        return divisors
    n, m = list(map(int, input().split()))
    for i in make_divisors(m):
        if m // i >= n:
            print(i)
            exit()

if __name__ == '__main__':
    main()
