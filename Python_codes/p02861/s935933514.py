import itertools
import math

def dist(c1, c2):
    dist = math.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)
    return dist

def solve():
    N = int(input())
    c = []
    for _ in range(N):
        x_tmp, y_tmp = list(map(int, input().split()))
        c.append([x_tmp, y_tmp])
    l = [i for i in range(N)]

    sum_dist = 0
    ave_dist = 0
    for p in itertools.permutations(l):
        for i in range(len(p)-1):
            sum_dist += dist(c[p[i]], c[p[i+1]])
    ave_dist = sum_dist/len(list(itertools.permutations(l)))
    print(ave_dist)

if __name__ == "__main__":
    solve()