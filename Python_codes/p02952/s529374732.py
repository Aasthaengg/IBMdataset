def actual(n):
    return len([i for i in range(1, n + 1) if len(str(i)) % 2 == 1])

    # nums = [i for i in range(1, n+1)]
    # return len([n for n in nums if len(str(n)) % 2 == 1])

n = int(input())
print(actual(n))