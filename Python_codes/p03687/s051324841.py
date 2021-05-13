s = input()


sl = list(s)


ans = 101

for i in range(26):
    cur_char = chr(ord('a') + i)

    if not cur_char in sl:
        continue

    sl_cp = sl.copy()

    while not len(set(sl_cp)) == 1:

        for i in range(len(sl_cp)-1):
            if sl_cp[i+1] == cur_char:
                sl_cp[i] = cur_char

        sl_cp.pop()

    ans = min(ans, len(sl) - len(sl_cp))

print(ans)
