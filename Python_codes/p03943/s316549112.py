candy_list = list(map(int, input().split(' ')))

if max(candy_list) == (sum(candy_list) - max(candy_list)):
    print('Yes')
else:
    print('No')
