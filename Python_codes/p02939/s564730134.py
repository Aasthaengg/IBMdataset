s = input()
maximum = [(0, [()])]

s = tuple(s)
for i in range(1, len(s) + 1):
    j = i - 1
    while j >= 0:
        max_count, previous = maximum[j]
        if max_count < 0:
            j -= 1
            continue
        current = s[j:i]
        if any(p != current for p in previous):
            if len(maximum) == i + 1:
                mc, blocks = maximum[i]
                if mc == max_count + 1:
                    blocks.append(current)
                break
            else:
                maximum.append((max_count + 1, [current]))
        j -= 1
    else:
        if len(maximum) != i + 1:
            maximum.append((-1, []))
    assert len(maximum) == i + 1

print(maximum[-1][0])