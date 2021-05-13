def main():
    n = int(input())
    As = list(map(int, input().split()))
    As_Count = [0] * (10**5+1)
    q = int(input())
    bcs = [list(map(int, input().split())) for _ in range(q)]
    for A in As:
        As_Count[A] += 1
    ans = sum(As)
    for b, c in bcs:
        ans -= As_Count[b] * b
        ans += c * As_Count[b]
        As_Count[c] += As_Count[b]
        As_Count[b] = 0
        print(ans)


if __name__ == "__main__":
    main()
