def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ave = sum(a) / n
    a2 = [(abs(a[i] - ave), i) for i in range(n)]
    a2 = sorted(a2)
    print(a2[0][1])


if __name__ == "__main__":
    solve()
