n = int(input())
l = [int(x) for x in input().split()]


def count(ls, front):
    # replace ls[0] by front
    res = abs(front - ls[0])
    sm = front
    for i in range(1, n):
        temp = ls[i]
        if sm > 0 and ls[i] > -sm-1:
            res += abs(-sm-1 - ls[i])
            temp = -sm-1
        elif sm < 0 and ls[i] < -sm+1:
            res += abs(-sm+1 - ls[i])
            temp = -sm+1
        sm += temp
    return res


ans = 0
if l[0] == 0:
    ans = min(count(l, 1), count(l, -1))
else:
    ans = min(count(l, l[0]), count(l, -l[0] // abs(l[0])))
print(ans)