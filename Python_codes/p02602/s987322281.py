n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n-k):
    if a[i] < a[i+k]:
        print("Yes")
    elif a[i] >= a[i+k]:
        print("No")
