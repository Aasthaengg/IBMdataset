import bisect

n = int(input())
as_ = list(map(int, input().split()))
bs_ = list(map(int, input().split()))
cs_ = list(map(int, input().split()))

as_.sort()
bs_.sort()
cs_.sort()

ans = 0
for b in bs_:
  ans += bisect.bisect_left(as_, b) * (n-bisect.bisect_right(cs_, b))
print(ans)