def g(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            yield " {}".format(i)
            continue
        x = i
        while x != 0:
            if x % 10 == 3:
                yield " {}".format(i)
                break
            x //= 10

n = int(input())
print("".join(g(n)))