n, a, b = map( int, input().split() )
sum = 0
count = 1

while count <= n:

    c_check = 0
    count_temp = count
    while 1:
        c_check += count_temp % 10
        count_temp = int(count_temp/10)
        if count_temp<1:
            break

    if a <= c_check and b >= c_check:
        sum += count

    count += 1


print("{}".format(sum))