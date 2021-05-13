int_num = int(input())
takahashi_can_calculation = set()

for i_left in range(1, 10):
    for i_right in range(1, 10):
        result = i_left * i_right
        takahashi_can_calculation.add(result)

if int_num in takahashi_can_calculation:
    print('Yes')
else:
    print('No')