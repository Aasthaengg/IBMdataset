def solve():
    X = int(input())
    years = 0
    amount = 100
    while amount < X:
        amount += amount // 100
        years += 1
    print(years)

if __name__ == "__main__":
    solve()