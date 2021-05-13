a_num, b_num = map(int, input().split())

result = a_num * b_num

if result % 2 == 0:
    print('Even')
else:
    print('Odd')
