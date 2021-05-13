
coin_500 = int(input())
coin_100 = int(input())
coin_50 = int(input())

target = int(input())

counter = 0


for i_500 in range(coin_500 + 1):
    # print('======= loop 500 =======')
    if i_500 * 500 > target:
        break

    for i_100 in range(coin_100 + 1):
        # print('-------- loop 100 ---------')
        if i_500 * 500 + i_100 * 100 > target:
            break

        for i_50 in range(coin_50 + 1):
            # print('........... loop 50 ..........')
            if i_500 * 500 + i_100 * 100 + i_50 * 50 == target:
                # print('match: ', i_500, i_100, i_50)
                counter += 1

print(counter)