from collections import deque
def queue():
    h = int(input())
    for i in range(h):
        s.append(s.popleft())

while True:
    s = input()
    if s == "-": break
    s = deque(s)
    m = int(input())
    for i in range(m):
        queue()
    print("{}".format("".join(s)))

