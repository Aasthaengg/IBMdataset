w0 = raw_input().lower()
c = 0
while True:
    s = raw_input()
    if s == 'END_OF_TEXT': break
    for w in s.lower().split():
        if w == w0:
            c += 1
print c
