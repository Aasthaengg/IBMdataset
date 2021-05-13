n, K = map(int, input().split())
A = [x-1 for x in list(map(int, input().split()))]

current = 0
d = dict()
d[current] = d.get(current, 0) + 1
pattern = [0]
cnt = K

while True:
    current = A[current]
    if d.get(current) == 2:
        break
    else:
        if d.get(current) == None:
            d[current] = d.get(current, 0) + 1
        else:
            d[current] = d.get(current) + 1
        pattern.append(current)
        cnt -= 1
        if cnt == 0:
            break

if cnt == 0:
    print(pattern[-1]+1)
else:
    loop = len([key for key, value in d.items() if value == 2])
    not_loop = len([key for key, value in d.items() if value != 2])
    pattern = pattern[not_loop:]
    ans_position = (K - not_loop) % loop

    print(pattern[ans_position]+1)