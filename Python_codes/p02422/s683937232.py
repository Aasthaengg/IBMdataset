st, q = input(), int(input())
for _ in range(q):
    order = list(map(str, input().split()))
    a, b = int(order[1]), int(order[2])
    if order[0] == "print":
        print(st[a:b+1])
    elif order[0] == "reverse":
        st = st[:a] + st[a:b+1][::-1] + st[b+1:]
    else:
        st = st[:a] + order[3] + st[b+1:]