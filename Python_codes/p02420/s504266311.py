while True:
    card = raw_input().strip()
    if card =="-":
        break
    shufflenum = int(raw_input().strip())
    for x in xrange(shufflenum):
        h = int(raw_input().strip())
        card = card[h:]+card[:h]
    print card