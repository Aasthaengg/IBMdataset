import bisect

N = int(input())
As = sorted(list(map(int, input().split())))
Bs = sorted(list(map(int, input().split())))
Cs = sorted(list(map(int, input().split())))

cnt = 0
for b in Bs:
    a_b = bisect.bisect_left(As,b)
    b_c = N - bisect.bisect_right(Cs, b)
    
    cnt += a_b * b_c
print(cnt)