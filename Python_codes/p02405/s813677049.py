def get_sharp_or_dot(number):
    if number % 2 == 0:
        return '#'
    else:
        return '.'


num = 0
while True:
    [H, W] = [int(x) for x in raw_input().split()]
    if [H, W] == [0, 0]:
        break
    for x in range(H):
        print("".join([get_sharp_or_dot(i) for i in range(x, W + x, 1)]))

    print('')