def main():
    import sys
    input = sys.stdin.readline
    from collections import Counter

    N = int(input())
    A = list(map(int,input().split()))
    total = sum(A)
    counter = Counter(A)
    Q = int(input())
    for _ in range(Q):
        b,c = map(int,input().split())
        total = total - b*counter[b] + c*counter[b]
        counter[c] += counter[b]
        counter[b] = 0
        print(total)

if __name__ == '__main__':
    main()
