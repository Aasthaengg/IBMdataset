def solve(n):
    return len(list(filter(lambda _: _=="2", list(n))))
n = input()
print(solve(n))