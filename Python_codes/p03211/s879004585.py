def actual(s):
    nums = [int(s[i:i + 3]) for i in range(len(s) - 2)]

    return min([abs(n - 753) for n in nums])

s = input()

print(actual(s))