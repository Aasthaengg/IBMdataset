N = int(input())

button_dict = dict()

for i in range(1,N+1):
    button_dict[i] = int(input())

pushed_button_set = set()
i = 1
while 1:
    if i in pushed_button_set:
        print(-1)
        break
    elif i == 2:
        print(len(pushed_button_set))
        break
    else:
        pushed_button_set.add(i)
        i = button_dict[i]