import itertools

N = int(input())
d_int_list = list(map(int, input().split()))
comb_list = list(itertools.combinations(d_int_list, 2))
ans = 0

for i in comb_list:
    ans += i[0] * i[1]

print(ans)
