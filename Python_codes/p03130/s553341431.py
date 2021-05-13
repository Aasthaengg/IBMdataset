from collections import defaultdict
def main():
    d = defaultdict(int)
    for _ in range(3):
        a, b = list(map(int, input().split()))
        d[a] += 1
        d[b] += 1
    if sorted(d.values()) == [1, 1, 2, 2]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
