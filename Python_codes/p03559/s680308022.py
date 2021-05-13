import bisect

N = int(input())
A = sorted([int(i) for i in input().split(" ")])
B = [int(i) for i in input().split(" ")]
C = sorted([int(i) for i in input().split(" ")])

ans = 0
for b in B:
    a = bisect.bisect_left(A, b) # 使えるAの要素数
    c = N - bisect.bisect_right(C, b) # 使えるCの要素数
    ans += a * c  

print(ans)