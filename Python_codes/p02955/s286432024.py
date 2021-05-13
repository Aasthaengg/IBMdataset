from heapq import heappush, heappop


def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            heappush(divisors, -i)
            if i != n // i:
                heappush(divisors, -(n // i))

    return divisors


def p_e():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)

    divisors = get_divisors(sum_A)
    n = len(divisors)
    for _ in range(n):
        h = -heappop(divisors)
        sub_list = []
        for a in A:
            sub_list.append(a % h)

        x = sum(sub_list)
        sub_list.sort()
        
        if sum(sub_list[:-x // h]) <= K:
            print(h)
            exit()

    print(0)


if __name__ == '__main__':
    p_e()
