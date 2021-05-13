from collections import defaultdict

def main():
    N, K = map(int, input().split())
    d = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        d[a] += b
    total = 0
    for v, freq in sorted(d.items()):
        total += freq
        if total >= K:
            print(v)
            exit()


if __name__ == '__main__':
    main()
