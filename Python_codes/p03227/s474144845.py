def solve(s):
    return s[::-1] if (len(s) == 3) else s

s = input()
print(solve(s))
