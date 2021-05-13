def main():
    n = int(input())
    prime_list = []
    i = 11
    while len(prime_list) < n:
        j = 2
        while j * j <= i:
            if i % j == 0:
                j = 0
                break
            j += 1
        if j:
            prime_list.append(i)
        i += 5
    print(" ".join(map(str, prime_list)))


if __name__ == '__main__':
    main()

