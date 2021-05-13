import bisect
N = input()
A = map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
A.sort()
B.sort()
C.sort()

BC_type_num = []
pre = 0
for b in reversed(B):
    upper_bound = bisect.bisect_right(C, b)
    BC_type_num.append(pre + N - upper_bound)
    pre += N - upper_bound
BC_type_num.reverse()

res = 0
for a in A:
    upper_bound = bisect.bisect_right(B, a)
    if upper_bound < N:
        res += BC_type_num[upper_bound]

print res