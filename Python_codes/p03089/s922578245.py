from collections import deque

N = int(input())
b_li = list(map(int, input().split()))
a_li = deque()
while len(b_li) > 0:
    found = False
    for i in range(len(b_li) - 1, -1, -1):
        if b_li[i] == i + 1:
            found = True
            a_li.appendleft(b_li[i])
            del b_li[i]
            break

    if not found:
        print(-1)
        exit()

for a in a_li:
    print(a)
