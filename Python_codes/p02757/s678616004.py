#coding:utf-8
import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7

    N,P = LMIIS()
    S = input()[::-1]
    R = [0]*P
    R[0] = 1
    b = 1
    r = 0


    if P == 2 or P == 5:
        ans = 0
        for i,c in enumerate(S):
            if int(c) % P == 0:
                ans += N-i
        print(ans)
        return

    for c in S:
        r += b * int(c)
        r %= P
        R[r] += 1
        b *= 10
        b %= P
    ans = 0

    for r in R:
        ans += r*(r-1)//2
    print(ans)
        

if __name__ == '__main__':
    main()