S = input()
Q = int(input())

forward = True
que0 = []
que1 = []

for _ in range(Q):
    query = input().split()

    if query[0] == '1':
        forward = not forward

    else:
        head = (query[1] == '1')
        if head ^ forward:
            que1.append(query[2])
        else:
            que0.append(query[2])

S = ''.join(que0[::-1]) + S + ''.join(que1)

if forward:
    print(S)
else:
    print(S[::-1])