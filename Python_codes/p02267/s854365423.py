def main():
    N = int(input())
    S = [int(_) for _ in input().split()]
    Q = int(input())
    T = [int(_) for _ in input().split()]

    ans = 0

    for t in T:
        for s in S:
            if s == t:
                ans += 1
                break

    print(ans)

main()

