S = input()
Q = int(input())

r = False
prefix = []
suffix = []
for _ in range(Q):
    query = input()
    if query == '1':
        r ^= True
    else:
        _, f, c = query.split()
        front = f == '1'

        if r ^ front:
            prefix.append(c)
        else:
            suffix.append(c)

if r:
    S = ''.join(suffix[::-1]) + S[::-1] + ''.join(prefix)
else:
    S = ''.join(prefix[::-1]) + S + ''.join(suffix)

print(S)
