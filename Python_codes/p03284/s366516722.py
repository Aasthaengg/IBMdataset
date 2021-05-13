# coding: utf-8

ans = 0

(n, k) = [int(i) for i in input().rstrip().split(" ")]
if n % k != 0:
    ans = 1


print(ans)
