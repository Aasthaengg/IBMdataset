def count_div_by_two(n: int):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


N = int(input())
A = list(map(int, input().split()))
count_A = list(map(count_div_by_two, A))
print(sum(count_A))
