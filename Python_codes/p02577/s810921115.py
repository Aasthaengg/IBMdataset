def solve(n):
    res = 0
    for x in n:
        res += int(x)
    return "Yes" if res % 9 == 0 else "No"

n = input()
print(solve(n))