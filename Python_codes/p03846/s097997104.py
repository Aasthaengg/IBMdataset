N = int(input())
A = sorted(map(int, input().split()))
print(pow(2, N >> 1, 10 ** 9 + 7) if (N & 1 and sorted(list(range(0, N, 2)) + list(range(2, N, 2))) == A) or (not N & 1 and sorted(list(range(1, N, 2)) + list(range(1, N, 2))) == A) else 0)