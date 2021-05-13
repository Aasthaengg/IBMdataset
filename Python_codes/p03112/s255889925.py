import sys
def main():
    input = sys.stdin.readline
    A,B,Q=map(int, input().split())
    S=[int(input()) for _ in range(A)]
    T=[int(input()) for _ in range(B)]
    X=[int(input()) for _ in range(Q)]
    from bisect import bisect_left
    INF=10**11
    S=[-INF] + S + [INF]
    T=[-INF] + T + [INF]
    for x in X:
        sr = bisect_left(S, x)
        tr = bisect_left(T, x)
        sl,tl=sr-1,tr-1
        ans=INF
        ans = min(ans, abs(S[sl]-T[tl]) + min(abs(S[sl]-x), abs(T[tl]-x)))
        ans = min(ans, abs(S[sl]-T[tr]) + min(abs(S[sl]-x), abs(T[tr]-x)))
        ans = min(ans, abs(S[sr]-T[tl]) + min(abs(S[sr]-x), abs(T[tl]-x)))
        ans = min(ans, abs(S[sr]-T[tr]) + min(abs(S[sr]-x), abs(T[tr]-x)))
        print(ans)

if __name__ == '__main__':
    main()