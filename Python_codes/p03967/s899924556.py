S = input()
p_count = 0
g_count = 0
win, lose = 0, 0
for s in S:
    if s == "g":
        if p_count < g_count:
            p_count += 1
            win += 1
        else:
            g_count += 1
    else:
        if p_count < g_count:
            p_count += 1
        else:
            g_count += 1
            lose += 1
print(win - lose)
