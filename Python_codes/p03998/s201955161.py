from collections import deque

sa = deque(input())
sb = deque(input())
sc = deque(input())

a = len(sa)
b = len(sb)
c = len(sc)


s = sa.popleft()
a -= 1
while True:
    if s == "a":
        a -= 1
        if a == -1:
            ans = "A"
            break
        else:
            s = sa.popleft()

    elif s == "b":
        b -= 1
        if b == -1:
            ans = "B"
            break
        else:
            s = sb.popleft()

    elif s == "c":
        c -= 1
        if c == -1:
            ans = "C"
            break
        else:
            s = sc.popleft()

print(ans)
