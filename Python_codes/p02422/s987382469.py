s = list(input())
n = int(input())
for i in range(n):
    order = input().split()
    a, b = int(order[1]), int(order[2])+1
    if order[0] == "replace":
        # s = s.replace(s[a:b],order[3])
        s[a:b] = order[3]
    elif order[0] == "reverse":
        t = s[a:b]
        # s = s.replace(s[a:b],t[::-1])
        s[a:b] = t[::-1]
    else:
        t = "".join(s[a:b])
        print(t)