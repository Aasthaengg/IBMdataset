from collections import deque
n = int(input())
v = list(map(int,input().split()))
v.sort(reverse=True)
stack = deque()
for i in v:
    stack.append(i)
while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        small1 = stack.pop()
        small2 = stack.pop()
        tmp = (small1 + small2)/2
        stack.append(tmp)