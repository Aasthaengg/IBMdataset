cd_list = [i for i in map(int, input().split())]
cd_list.sort(reverse=True)
if cd_list[0] == cd_list[1] + cd_list[2]:
    print('Yes')
else:
    print('No')