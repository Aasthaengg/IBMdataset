import collections

sa = collections.deque(input())
sb = collections.deque(input())
sc = collections.deque(input())


tmp = "a"
while True:
    if tmp == "a":
        try:
            tmp = sa.popleft()
        except(IndexError):
            print("A")
            exit()
    elif tmp == "b":
        try:
            tmp = sb.popleft()
        except(IndexError):
            print("B")
            exit()
    else:
        try:
            tmp = sc.popleft()
        except(IndexError):
            print("C")
            exit()
    
