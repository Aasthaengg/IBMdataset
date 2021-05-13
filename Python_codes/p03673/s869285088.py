from collections import deque

n = int(input())
a_li = list(map(int, input().split()))
b_li = deque()
for i in range(len(a_li)):
    if i % 2 == 0:
        b_li.append(a_li[i])
    else:
        b_li.appendleft(a_li[i])

if len(a_li) % 2 == 0:
    print(*b_li)
else:
    print(*list(b_li)[::-1])
