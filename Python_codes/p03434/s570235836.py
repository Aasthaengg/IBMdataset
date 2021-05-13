N = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)

target_num = sum(a_list[::2]) - sum(a_list[1::2])
print(target_num)