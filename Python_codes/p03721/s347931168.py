from collections import defaultdict
def main():
    n, k = map(int, input().split())
    D = defaultdict(int)
    for _ in range(n):
        a, b = map(int, input().split())
        D[a] += b
    for d in sorted(D.items(), key = lambda x: x[0]):
        k -= d[1]
        if k <= 0:
            print(d[0])
            break

if __name__ == '__main__':
    main()
