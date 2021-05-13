
n = int(input())

div_cnt = [0] * n

def search_div(data, n):
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                data[i - 1] += 1
                n = int(n / i)
                break
        

for i in range(2, n + 1):
    search_div(div_cnt, i)

cnt_2 = 0
cnt_4 = 0
cnt_14 = 0
cnt_24 = 0
cnt_74 = 0
if max(div_cnt) < 4:
    print(0)
    exit()

for i in range(n):
    if div_cnt[i] >= 74:
        cnt_2 += 1
        cnt_4 += 1
        cnt_14 += 1
        cnt_24 += 1
        cnt_74 += 1
    elif div_cnt[i] >= 24:
        cnt_2 += 1
        cnt_4 += 1
        cnt_14 += 1
        cnt_24 += 1
    elif div_cnt[i] >= 14:
        cnt_2 += 1
        cnt_4 += 1
        cnt_14 += 1
    elif div_cnt[i] >= 4:
        cnt_2 += 1
        cnt_4 += 1
    elif div_cnt[i] >= 2:
        cnt_2 += 1
    
ans = cnt_74 + cnt_24 * (cnt_2 - 1) + cnt_14 * (cnt_4 - 1) + (cnt_4 * (cnt_4 - 1)) / 2 * (cnt_2 - 2)
print(int(ans))