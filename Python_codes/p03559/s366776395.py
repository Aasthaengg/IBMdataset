from bisect import bisect,bisect_left

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

ans = 0

for b in B:
    ca = bisect_left(A,b)
    cc = N - bisect(C,b)
    ans += ca*cc

print(ans)