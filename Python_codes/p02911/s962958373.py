n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
charenger = [k - q] * n
for i in range(q):
    charenger[a[i] - 1] += 1

for out in charenger:
    if out > 0:
        print("Yes")
    else:
        print("No")
