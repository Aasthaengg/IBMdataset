n = int(input())
l_list = list(map(int, input().split()))

if sum(l_list) - 2* max(l_list) > 0:
    print('Yes')
else:
    print('No')