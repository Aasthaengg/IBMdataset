while 1:
    w=str(raw_input())
    if w == '-':
        break
    m = int(raw_input())
    for i in range(m):
       h = int(raw_input())
       w = w [h:] + w[:h]
    print w