from collections import Counter
from itertools import permutations

def main():
    N, C = map(int, input().split())
    D = tuple(tuple(map(int, input().split())) for _ in range(C))

    cnt = [Counter() for _ in range(3)]

    for i in range(N):
        c = [int(x)-1 for x in input().split()]
        for j in range(3):
            cnt[j].update(c[(3-(i+2)+j)%3::3])

    ans = 1000*500*500+5
    for p in permutations(range(C), 3):
        s = 0
        for j in range(3):
            s += sum(D[k][p[j]] * v for k, v in cnt[j].items())
        if s < ans: ans = s
    print(ans)

main()
