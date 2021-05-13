def solve(s):
    return "YES" if 7 >= s.count("x") else "NO"

s = input()
print(solve(s))