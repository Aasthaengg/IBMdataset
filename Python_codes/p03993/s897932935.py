# B - 仲良しうさぎ
# https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_b

n = int(input())
A = list(map(int, input().split()))

ans = 0
for itr, a in enumerate(A):
  if a - 1 > itr and A[a - 1] == itr + 1:
    ans += 1

print(ans)
