def solve(target):
    n = int(target / 100)
    if n * 100 <= target <= n * 105:
        print(1)
    else:
        print(0)

solve(int(input()))