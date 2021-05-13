import sys
import itertools

# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    S = list(input())

    l = []
    down = 0  # "0"
    up = 0  # "1"
    flag = int(S[0])
    if not flag:
        l.append(0)
    for i in range(N):

        if int(S[i]) == 1:
            up += 1
            if down:
                l.append(down)
                down = 0
        if int(S[i]) == 0:
            down += 1
            if up:
                l.append(up)
                up = 0
    if up:
        l.append(up)
    else:
        l.append(down)

    if len(l)<=2*K+1:
        print(N)
        exit()
    total = sum(l[:2*K+1])
    ans =total
    flag =1
    csum=list(itertools.accumulate(l))
    for i in range(2,len(l) - 2 * K +1,2):
        right =min(i+2*K,len(l)-1)
        ans = max(ans, csum[right] - csum[i-1])

    print(ans)

if __name__ == "__main__":
    main()
