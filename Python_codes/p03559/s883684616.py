from bisect import bisect_left
from bisect import bisect_right
N = int(input())
As = sorted(list(map(int, input().split())))
Bs = sorted(list(map(int, input().split())))
Cs = sorted(list(map(int, input().split())))


cnt = 0
for b in Bs:
    ind_c = bisect_left(Cs,b+1)
    ind_a = bisect_right(As,b-1)
    if ind_c == N:continue
    # print(b,ind_a,ind_c)
    cnt += (N - ind_c) * (ind_a)
print(cnt)
