s = input()
len_s = len(s)
def calc_one_sum(n):
    r = len_s
    l = len_s - 1
    i = 0
    one_sum = 0
    while l > 0:
        if n & 1<<i != 0:
            one_sum += int(s[l:r])
            r = l
            l -= 1
        else:
            l -= 1
        i += 1
    one_sum += int(s[l:r])
    return one_sum
ans = 0
for i in range(2**(len_s - 1)):
    ans += calc_one_sum(i)
print(ans)