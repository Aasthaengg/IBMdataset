def actual(n):
    is_zorome = lambda num: len(set(str(num))) == 1

    for i in range(100, 1000):
        if i >= n and is_zorome(i):
            return i

n = int(input())
print(actual(n))