def solve():
    n = int(input())
    a = list(map(int, input().split()))
    cost = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            cost += 1
            a[i+1] = -1
    print(cost)
    return 0

if __name__ == "__main__":
    solve()