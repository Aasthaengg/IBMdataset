n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

high = 10**18+1
low = -1

while high-low>1:
    res = k
    mid = (low+high)//2
    for i in range(n):
        res -= max(0, a[i]-(mid//b[i]))
    if res < 0: low = mid
    else: high = mid
print(high)