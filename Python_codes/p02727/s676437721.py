from heapq import*


x, y, a, b, c = map(int, input().split())

P = sorted(map(int, input().split()), reverse = True)[:x]
Q = sorted(map(int, input().split()), reverse = True)[:y]
R = sorted(map(int, input().split()))

heapify(P); heapify(Q)
while R:
    p, q, r = heappop(P), heappop(Q), R.pop()
    if p < q:
        heappush(Q, q)
        if p < r:
            heappush(P, r)
        else:
            heappush(P, p)
            break
    else:
        heappush(P, p)
        if q < r:
            heappush(Q, r)
        else:
            heappush(Q, q)
            break

print(sum(P) + sum(Q))
