n = int(input())
x = input()
original_pop_cnt = x.count("1")

pop_cnt_add = original_pop_cnt + 1
pop_cnt_sub = original_pop_cnt - 1

n_after_once_popcount_add = 0
n_after_once_popcount_sub = 0

for i in range(n):
    n_after_once_popcount_add = (n_after_once_popcount_add * 2 + int(x[i])) % pop_cnt_add
    if pop_cnt_sub != 0:
        n_after_once_popcount_sub = (n_after_once_popcount_sub * 2 + int(x[i])) % pop_cnt_sub

pow_add = [1] * 250000
pow_sub = [1] * 250000
for i in range(1, n + 100):
    pow_add[i] = (pow_add[i-1]*2) % pop_cnt_add
    if pop_cnt_sub != 0:
        pow_sub[i] = (pow_sub[i-1]*2) % pop_cnt_sub

def f(nex):
    ans = 0
    num = nex
    while num != 0:
        num = num % bin(num).count("1")
        ans += 1
    return ans

for i in range(n-1, -1, -1):
    if x[n - 1 - i] == "0":
        nxt = n_after_once_popcount_add
        nxt = nxt + pow_add[i]
        nxt = nxt % pop_cnt_add
        print(f(nxt) + 1)
    if x[n - 1 - i] == "1":
        if pop_cnt_sub != 0:
            nxt = n_after_once_popcount_sub
            nxt = nxt - pow_sub[i]
            nxt = nxt % pop_cnt_sub
            print(f(nxt) + 1)
        else:
            print(0)


