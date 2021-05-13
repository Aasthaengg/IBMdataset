import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K, A, B = mapint()
if (B-A)/2<=1:
    print(K+1)
else:
    cnt = A
    rest = K - cnt + 1
    if rest<2:
        print(K+1)
    else:
        if rest%2==0:
            print(cnt+(B-A)*rest//2)
        else:
            rest -= 1
            cnt += 1
            print(cnt+(B-A)*rest//2)