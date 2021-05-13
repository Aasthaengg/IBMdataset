n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
for a_r in a[k:]:
    if a[l] < a_r:
        print("Yes")
    else:
        print("No")
    l += 1
