import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
orders = []
for i in range(n):
    orders.append(input().strip())

#orders = ["insert 5","insert 2","insert 3","insert 1","delete 3","insert 6","delete 5"]
#orders = ["insert 5","insert 2","insert 3","insert 1","delete 3","insert 6","delete 5","deleteFirst","deleteLast"]

data = deque()
for d in orders:
    if " " in d:
        order, value = d.split(" ")
    else:
        order = d

    if order == "insert":
        data.appendleft(value)
    elif order == "delete":
        try:
            data.remove(value)
        except ValueError:
            pass
    elif order == "deleteFirst":
        data.popleft()
    elif order == "deleteLast":
        data.pop()
    else:
        print('Unknown order')

# print result
print(" ".join(data))


