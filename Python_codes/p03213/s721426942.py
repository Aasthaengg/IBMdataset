
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

def count_num(data, n):
    cnt = 0
    for i in range(len(data)):
        if data[i] >= n - 1:
            cnt += 1
    
    return cnt
print(int(count_num(div_cnt, 75) + count_num(div_cnt, 25) * (count_num(div_cnt, 3) - 1) + count_num(div_cnt, 15) * (count_num(div_cnt, 5) - 1) + count_num(div_cnt, 5) * (count_num(div_cnt, 5) - 1) / 2 * (count_num(div_cnt, 3) - 2)))