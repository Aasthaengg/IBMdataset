def actual(X):
    pow_nums = [1]

    for i in range(2, 40 + 1):
        for j in range(2, 40 + 1):
            if i ** j <= 1000:
                pow_nums.append(i ** j)

    pow_nums = sorted(set(pow_nums))

    return [pow_num for pow_num in pow_nums if pow_num <= X][-1]


X = int(input())
print(actual(X))
