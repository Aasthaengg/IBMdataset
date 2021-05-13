n, m = map(int, input().split())
s = input()[::-1]

position = 0
steps = []
while position < n:
    position_ = position
    for l in range(m, 0, -1):
        if position+l > len(s)-1:
            continue
        if s[position+l] == '0':
            position += l
            steps.append(l)
            break
    if position == position_:
        steps = [-1]
        break
print(*steps[::-1])