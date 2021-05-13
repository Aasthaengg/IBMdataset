a = ord('a')
counts = [0] * 26
while 1:
    try:
        raw = input()
    except EOFError:
        break
    for c in raw.lower():
        if 0 <= ord(c) - a < 26:
            counts[ord(c) - a] += 1
for i, count in enumerate(counts):
    print('%s : %d' % (chr(a + i), count))