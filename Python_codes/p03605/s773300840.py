num_input = int(input())
set_of_nine = set()

for i in range(9, 100, 10):
    set_of_nine.add(i)

for tmp in range(90, 100, 1):
    set_of_nine.add(tmp)

if num_input in set_of_nine:
    print('Yes')
else:
    print('No')
