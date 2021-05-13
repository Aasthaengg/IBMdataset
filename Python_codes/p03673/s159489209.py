from collections import deque
n = int(input())
a_list = [int(x) for x in input().split()]
left_flag = n % 2 == 1
d = deque()
for a in a_list:
    if left_flag:
        d.appendleft(a)
    else:
        d.append(a)
    left_flag = not left_flag
print(*d)