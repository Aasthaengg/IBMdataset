from collections import deque
h,w = map(int,input().split())
s = "#"

print(s*(w+2))

for i in range(h):
    lst = deque(list(map(str,input().split())))
    lst.appendleft("#")
    lst.append("#")
    print("".join(lst))

print(s*(w+2)) 