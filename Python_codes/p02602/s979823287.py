n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k+1, n+1):
    i -= 1
    if a[i-k] < a[i]:
        print("Yes")
    else:
        print("No")
