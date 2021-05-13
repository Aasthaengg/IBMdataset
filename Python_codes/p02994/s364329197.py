N, L = map(int, input().split())
if L >= 0:
    print(sum(range(L + 1, L + N)))
elif N + L - 1 >= 0:
    print(sum(range(L, L + N)))
else:
    print(sum(range(L, L + N - 1)))