in_list = input().split(' ')
N = int(in_list[0])
A = int(in_list[1])
B = int(in_list[2])

count = 0
for i in range(N+1):
    if i == 10000:
        i_4 = 1
        res_i = 0
    else:
        i_4 = 0
        res_i = i

    i_3 = int(res_i/1000)
    if i_3 != 0:
        res_i = res_i - i_3*1000
    
    i_2 = int(res_i/100)
    if i_2 != 0:
        res_i = res_i - i_2*100
    
    i_1 = int(res_i/10)
    if i_1 != 0:
        res_i = res_i - i_1*10
    
    i_0 = res_i
    i_sum = i_4 + i_3 + i_2 + i_1 + i_0
    # print('i_sum：', i_sum)
    # print(i_4, i_3, i_2, i_1, i_0)

    if i_sum >= A and i_sum <= B:
        count += i
        # print('clear i_sum：', i_sum)
        # print('clear', i_4, i_3, i_2, i_1, i_0)

print(count)