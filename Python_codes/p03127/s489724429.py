# https://atcoder.jp/contests/abc118/tasks/abc118_c

n = int(input())
A = [int(i) for i in input().split()]

ans = A[0]
for a in A[1:]:
    if ans > a:
        ans, a = a, ans  # ansが常に小さくなるようにする。
    while a % ans != 0:
        a = a % ans
        a, ans = ans, a
    if ans == 1:
        print(1)
        quit()

print(ans)
