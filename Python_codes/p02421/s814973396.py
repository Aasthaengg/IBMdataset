n = int(input())
taro = 0
hana = 0

for _ in range(n):
    idiom_list = list(input().split(' '))
    sort_list = sorted(idiom_list)
    if idiom_list[0] == idiom_list[1]:
        taro += 1
        hana += 1
    else:
        if idiom_list == sort_list:
            hana += 3
        else:
            taro += 3

print('{a} {b}'.format(a=taro, b=hana))

