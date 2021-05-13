import bisect

n = int(input())
a_list = [int(x) for x in input().split()]
b_list = [int(x) for x in input().split()]
c_list = [int(x) for x in input().split()]

a_list = sorted(a_list)
b_list = sorted(b_list)
c_list = sorted(c_list)

ans = 0

for b_i in b_list:
    a_count_i = bisect.bisect_left(a_list,b_i)
    c_count_i = len(c_list) - bisect.bisect_right(c_list,b_i)
    ans += a_count_i * c_count_i

print(ans)