n, k = list(map(int, input().split()))
xs = [0 for i in range(n)]

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for y in a:
        xs[y - 1] += 1

print(sum([1 if x == 0 else 0 for x in xs]))
