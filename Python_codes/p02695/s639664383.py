import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m, q = map(int, input().split())
    comb = [list(map(int, input().split())) for _ in range(q)]
    max_ = 0
    for i in itertools.combinations_with_replacement(range(1,m+1), n):
        point = 0
        for j in comb:
            if i[j[1]-1] - i[j[0]-1] == j[2]:
                point += j[3]
        max_ = max(max_, point)
    print(max_)

if __name__ == '__main__':
    main()