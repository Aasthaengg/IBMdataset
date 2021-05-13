from heapq import heappush, heappop

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # heappush(heap, (-(a[i]+b[j]+c[k]), i, j, k))
    heap = []
    heappush(heap, (-(a[0]+b[0]+c[0]), 0, 0, 0))
    s = set()
    for _ in range(k):
        value, i, j, k = heappop(heap)
        print(-value)
        if (i+1, j, k) not in s and i < x - 1:
            s.add((i+1, j, k))
            heappush(heap, (-(a[i+1]+b[j]+c[k]), i+1, j, k))
        if (i, j+1, k) not in s and j < y - 1:
            s.add((i, j+1, k))
            heappush(heap, (-(a[i]+b[j+1]+c[k]), i, j+1, k))
        if (i, j, k+1) not in s and k < z - 1:
            s.add((i, j, k+1))
            heappush(heap, (-(a[i]+b[j]+c[k+1]), i, j, k+1))

main()