n, *a_l= map(int, open(0).read().split())
odd = 1
for a in a_l:
    tmp_odd = 0
    for i in [a-1, a, a+1]:
        if i % 2 == 1:
            tmp_odd += 1
    odd *= tmp_odd
ans = 3**n - odd
print(ans)