from collections import deque
N = int(input())

x_list=deque()

for i in range(N):
    a = input().split()
    if a[0] == "insert":
        x_list.appendleft(a[1])
    elif a[0] == "delete":
        try:
            x_list.remove(a[1])
        except:
            pass
    elif a[0] == "deleteFirst":
        x_list.popleft()
    else:
        x_list.pop()

print(*x_list)
