import bisect
A, B, Q = map(int, input().split())
S = list(int(input()) for _ in range(A)) 
T = list(int(input()) for _ in range(B))


for _ in range(Q):
    x = int(input())
    s = bisect.bisect_right(S, x)
    t = bisect.bisect_right(T, x)
    s %= A
    t %= B
    ans = 2*10**10
    for i in range(2):
        for j in range(2):
            ans = min(ans, min(abs(x-S[s-i])+abs(S[s-i]-T[t-j]), abs(x-T[t-j])+abs(T[t-j]-S[s-i])))
    print(ans)
