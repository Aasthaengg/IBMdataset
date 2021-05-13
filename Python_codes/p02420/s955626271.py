words = []
while True:
    word = raw_input()
    if word == '-':
        break
    m = int(raw_input())
    buf = word
    for i in range(m):
        h = int(raw_input())
        buf += buf[:h]
        buf = buf[h:h+len(word)]
    words.append(buf)
for word in words:
    print word