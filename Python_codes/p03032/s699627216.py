import heapq
n, k = map(int, input().split())
v = list(map(int, input().split()))

y = min(n, k)

ans = 0

for i in range(y):
    cnt = 0
    heap = []
    for j in range(i+1):
        if v[j] < 0:
            heap.append(v[j])
            ans = max(ans, cnt)
        cnt += v[j]
        ans = max(ans, cnt)

    rest = k - i - 1
    right = n - i - 1
    for r in range(min(rest, right)+1):
        index = -1
        cnt2 = cnt
        heap2 = heap[:]
        for _ in range(r):
            cnt2 += v[index]
            if v[index] < 0:
                heap2.append(v[index])
            index -= 1

        ans = max(ans, cnt2)
        rest2 = rest - r
        heap2.sort()
        for o in range(rest2):
            if o >= len(heap2):
                break
            cnt2 -= heap2[o]
            ans = max(ans, cnt2)

print(ans)