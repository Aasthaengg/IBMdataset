N = int(input())

max_num = -1
max_count = -1
for num in range(1,N+1):
    num_orig = num
    count = 0
    while 1:
        amari = num%2
        if amari == 0:
            num = num // 2
            count += 1
        else:
            break
    if count > max_count:
        max_num = num_orig
        max_count = count

print(max_num)