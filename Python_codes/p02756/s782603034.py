S = list(input())
Q = int(input())
reverse, front, tail = False, [], []

for q in range(Q):
    query = list(input().split())

    if len(query) == 1:
        reverse ^= 1

    elif len(query) == 3:
        f, c = int(query[1]), query[2]
        f -= 1

        if f ^ reverse:
            tail.append(c)
        else:
            front.append(c)

if reverse:
    print(''.join((front[::-1] + S + tail)[::-1]))
else:
    print(''.join(front[::-1] + S + tail))
