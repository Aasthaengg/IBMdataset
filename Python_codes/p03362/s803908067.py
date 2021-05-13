N = int(input())

MAX = 55555


def create_prime_list(n):
    if n < 2:
        return []
    prime_list = [2]
    x = 3
    while x <= n:
        flag = False
        for p in prime_list:
            if x < p ** 2:
                flag = True
                break
            if x % p == 0:
                break
        if flag:
            prime_list.append(x)
        x += 2
    return prime_list


def main():
    prime_list = create_prime_list(MAX)
    w = [x for x in prime_list if x % 5 == 1]
    print(*w[:N])
    

if __name__ == "__main__":
    main()
