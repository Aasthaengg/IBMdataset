s = list(input())
n = len(s)


ans = 0

for i in range(2 ** (n-1)):
    s_temp = s.copy()
    numbers = [s_temp.pop(0)]
    for j in range(n-1):
        if (i >> j) & 1:
            numbers.append(s_temp.pop(0))
        else:
            numbers[len(numbers)-1] = numbers[len(numbers)-1] + s_temp.pop(0)

    numbers = list(map(int, numbers))

    ans += sum(numbers)

print(ans)
