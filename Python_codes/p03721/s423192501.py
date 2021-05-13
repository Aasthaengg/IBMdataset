def answer(arr, k):
    arr = sorted(arr, key=lambda a:a[0])
    for a, b in arr:
        if k > b:
            k -= b
        else:
            return a

n, k = map(int, input().split())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
print(answer(arr, k))