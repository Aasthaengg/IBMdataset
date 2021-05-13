m, k = input().split()
m, k = int(m), int(k)


xx = 0
for i in range(2**m):
    xx = xx ^ i

if k == 0:
    arr = [0] * (2 ** (m+1))
    for i in range(2**m):
        arr[2*i] = i
        arr[2*i+1] = i
    print(" ".join([str(x) for x in arr]))
elif xx != 0 or k >= 2 ** m:
    print(-1)
else:
    arr = [0] * (2 ** (m+1))
    f = (2 ** (m+1))
    arr[0] = k
    arr[f//2] = k
    pt1 = f // 2 - 1
    pt2 = f // 2 + 1
    curr = 0
    for i in range((f - 2) // 2):
        if (curr == k):
            curr += 1
        arr[pt1] = curr
        arr[pt2] = curr
        pt1 -= 1
        pt2 += 1 
        curr += 1
    print(" ".join([str(x) for x in arr]))
