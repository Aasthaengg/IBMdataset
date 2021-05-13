n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n-k):
    ab = a[i]
    aa = a[k+i]
    if aa > ab:
        print("Yes")
    else:
        print("No")