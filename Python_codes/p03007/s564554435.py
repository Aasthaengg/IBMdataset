from collections import deque

N = int(input())
a = deque(sorted(map(int, input().split())))


max_a = a.pop()
min_a = a.popleft()

ans_s = ""
while True:
    if len(a) <= 0:
        ans_s += "{} {}\n".format(max_a, min_a)
        ans = max_a - min_a
        break

    if max_a <= 0:
        ans_s += "{} {}\n".format(max_a, min_a)
        max_a -= min_a

        min_a = a.popleft()
    elif min_a >= 0:
        ans_s += "{} {}\n".format(min_a, max_a)
        min_a -= max_a

        max_a = a.pop()
    else:
        w = a.pop()
        if w < 0:
            ans_s += "{} {}\n".format(max_a, w)
            max_a -= w
        else:
            ans_s += "{} {}\n".format(min_a, w)
            min_a -= w

print(ans)
print(ans_s, end="")

