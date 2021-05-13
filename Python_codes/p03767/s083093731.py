N = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
print(sum([a[i] for i in range(1, 2 * N + 1, 2)]))