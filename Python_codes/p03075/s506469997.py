import itertools

antenna = [int(input()) for _ in range(6)]
distance = antenna.pop()
flag = True
for i in itertools.combinations(antenna, 2):
    if abs(i[0] - i[1]) > distance:
        print(':(')
        flag = False
        break
if flag:
    print('Yay!')