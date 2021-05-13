from collections import deque
import copy

n = int(input())
s = str(input())

dq_s = deque([])
for x in s:
    dq_s.append(x)

dq_s_shift = copy.deepcopy(dq_s)

ans = 0

for i in range(n):
    dq_s_shift.appendleft('_')
    count = 0
    # print(s)
    # print(s_shift)

    for j in range(i+1,n):
        if dq_s[j] == dq_s_shift[j]:
            count += 1
        else:
            count = 0
        if count >= ans and count <= i+1:
            ans = count
    # print('-'*30)
    # print(ans)

print(ans)