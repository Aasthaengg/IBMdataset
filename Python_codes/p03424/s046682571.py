snack_num = int(input())
a = map(str, input().split())
color_set = set(a)

if len(color_set) == 3:
    print('Three')
else:
    print('Four')
