import heapq
def main():
    N, Q = map(int, input().split())
    l = []
    for _ in range(N):
        s, t, x = map(int, input().split())
        l.append((s-x, 1, x))
        l.append((t-x, 0, x))
    for i in range(Q):
        d = int(input())
        l.append((d, 2, i))
    r = [-1] * Q
    l.sort()
    h = []
    se = set()
    for a, b, c in l:
        if b == 0:
            se.remove(c)
        elif b == 1:
            se.add(c)
            heapq.heappush(h, c)
        else:
            while h and h[0] not in se:
                heapq.heappop(h)
            r[c] = h[0] if h else -1
    print('\n'.join(map(str, r)))
            
main()
