N = int(input())
a_list = []
for i in range(N):
    a_list.append(int(input()))

has_pushed_button = set()
pushed_button_num = 1
count = 0
can_push_2 = False
while not pushed_button_num in has_pushed_button:
    has_pushed_button.add(pushed_button_num)
    pushed_button_num = a_list[pushed_button_num - 1]
    count += 1
    if pushed_button_num == 2:
        can_push_2 = True
        break

if can_push_2:
    print(count)
else:
    print(-1)