ran = int(input())
list_a = [int(a) for a in input().split()]
list_a.reverse()
for i in range(int(ran)):
    if not i == ran-1:
        print('{} '.format(list_a[int(i)]), end = '')
    else:
        print('{}'.format(list_a[int(i)]))
