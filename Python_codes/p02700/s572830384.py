import math
A, B, C, D = map(int, input().split())
t_mon = [A, B]
a_mon = [C, D]
t_turn = math.ceil(t_mon[0] / a_mon[1])
a_turn = math.ceil(a_mon[0] / t_mon[1])

if t_turn >= a_turn:
    print('Yes')
else:
    print('No')