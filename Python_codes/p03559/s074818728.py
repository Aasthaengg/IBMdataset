import bisect
N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

ans = 0
for b in B:
    ai = bisect.bisect_left(A, b)
    ci = bisect.bisect_right(C, b)
    ans += ai * (N-ci)
    #print(b,ai,ci)

print(ans)