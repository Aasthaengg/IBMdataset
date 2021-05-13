from collections import defaultdict
def main():
    n, k = list(map(int, input().split()))
    d = defaultdict(int)
    for _ in range(n):
        a, b = list(map(int, input().split()))
        d[a] += b
    A = sorted(d.items(), key = lambda x: x[0])
    count = 0
    for a in A:
        count += a[1]
        if count >= k:
            print(a[0])
            exit()

if __name__ == '__main__':
    main()
