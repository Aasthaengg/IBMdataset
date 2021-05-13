from collections import Counter


def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    counter = Counter(A)
    n_kind = len(counter.keys())
    if n_kind <= K:
        print(0)
    else:
        counts = list(counter.values())
        counts.sort()
        print(sum(counts[:(n_kind - K)]))



if __name__ == '__main__':
    main()