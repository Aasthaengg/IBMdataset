import sys
def main():
    input = sys.stdin.readline
    N,C=map(int, input().split())
    D=[tuple(map(int, input().split())) for _ in range(C)]
    c=[tuple(map(int, input().split())) for _ in range(N)]

    c0=[c[i][j]-1 for i in range(N) for j in range(N) if (i+j)%3==0]
    c1=[c[i][j]-1 for i in range(N) for j in range(N) if (i+j)%3==1]
    c2=[c[i][j]-1 for i in range(N) for j in range(N) if (i+j)%3==2]

    from collections import Counter
    cc=[Counter(c0), Counter(c1), Counter(c2)]

    ans = 10**10
    from itertools import permutations
    for colors in permutations(range(C), 3):
        tmp = 0
        for i,cci in enumerate(cc):
            for k,v in cci.items():
                tmp += D[k][colors[i]] * v
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    main()