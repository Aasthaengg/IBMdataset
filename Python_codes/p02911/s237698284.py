n, k, q = map(int, input().split())
a = [0] * n
for _ in range(q):
    a[int(input()) - 1] += 1
for x in a:
    if k - (q - x) <= 0:
        print("No")
    else:
        print("Yes")