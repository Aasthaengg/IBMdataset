import bisect
n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
b = [int(i) for i in input().split()]
b = sorted(b)
c = [int(i) for i in input().split()]
c = sorted(c)
ans = 0
for i in range(n):
    B = b[i]
    a_nums = bisect.bisect_left(a,B)
    c_nums = n - bisect.bisect_right(c,B)
    ans += a_nums * c_nums
print(ans)