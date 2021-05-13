n = input()
int_n = int(n)
len_n = len(n)
ans = sum([int(i) for i in n])

for i in range(len_n):
    target = int(n[:i+1][-1]) -1
    if target < 0:
        continue
    tmp_n = n[:i] + str(target) + '9'* (len_n - i - 1)
    tmp_n_ans = sum([int(i) for i in tmp_n])
    ans = max(tmp_n_ans, ans)
print(ans)