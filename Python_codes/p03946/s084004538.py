N, T = map(int, input().split())
A = list(map(int, input().split()))

pre = 10 ** 18
diff_max = 0
diff_cnt = 0

for a in A:
    if a < pre:
        pre = a
        continue

    if a - pre > diff_max:
        diff_max = a - pre
        diff_cnt = 1
    elif a - pre == diff_max:
        diff_cnt += 1

# 高橋君はdiffmax*(T//2)の利益
# 取引できるのがdiffcnt箇所、これをつぶす
print(diff_cnt)