def solve():
    n = int(input())
    p = list(map(int, input().split()))
    cost = 0
    for i in range(n-1):
        if p[i] != i+1:
            cost += 1
    if cost <= 2:
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == '__main__':
    solve()