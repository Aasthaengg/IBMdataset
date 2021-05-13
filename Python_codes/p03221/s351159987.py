from bisect import bisect_left

def solve():
    N,M = map(int, input().split())
    cities_in_prefecture = [[] for _ in range(N)]
    city_ids = []
    PYs = []
    for _ in range(M):
        P,Y = map(int, input().split())
        PYs.append((P,Y))
        cities_in_prefecture[P-1].append(Y)
    for p in range(N): cities_in_prefecture[p].sort()
    for P, Y in PYs:
        x = bisect_left(cities_in_prefecture[P-1], Y)
        # print(x, cities_in_prefecture[P-1])
        print('{0:06d}{1:06d}'.format(P, x+1), flush=True)
        
solve()