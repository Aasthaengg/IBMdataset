from collections import defaultdict

def main():
    N, M = map(int, input().split())
    a_b_dict = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        a_b_dict[a] += b
    ans = 0
    for a, b in sorted(a_b_dict.items()):
        if M >= b:
            M -= b
            ans += a * b
        else:
            ans += a * M
            break
    print(ans)


if __name__ == '__main__':
    main()
