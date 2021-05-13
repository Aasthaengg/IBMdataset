import sys
input = sys.stdin.readline
def main():
    N = int(input())
    C = [list(map(int, input().split())) for i in range(N)]
    ans = N
    for a,b in C:
        for x, y in C:
            if a == x and b == y:
                continue
            p, q = a -x , b - y
            CNT = 0
            for u, v in C:
                for s, t in C:
                    if u == s and v == t:
                        continue
                    if u-s == p and v-t == q:
                        CNT += 1
            ans = min(ans, N-CNT)
    print(ans)

if __name__ == '__main__':
    main()