import sys
lines = [line.strip() for line in sys.stdin]
cards = lines[0]
m = int(lines[1])
lines_index = 2
while m > 0:
    line = lines[lines_index]
    if line == '-':
        break
    h = int(line)
    cards = cards[h:] + cards[:h]
    m -= 1
    if m == 0:
        print (cards)
        lines_index += 1
        cards = lines[lines_index]
        if cards == '-':
            break
        lines_index += 1
        m = int(lines[lines_index])
    lines_index += 1