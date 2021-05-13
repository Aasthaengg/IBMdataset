def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    ans = 0
    AB = []
    for _ in range(N):
        a, b = map(int, input().split())
        ans -= b
        AB.append(a+b)
    AB.sort()

    for i in range(N):
        if i % 2 == 0:
            ans += AB.pop()
        else:
            AB.pop()
    print(ans)

if __name__ == "__main__":
    main()