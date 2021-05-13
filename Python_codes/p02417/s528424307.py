D = [0 for i in range(26)]
while True:
    s = ''
    try:
        s = raw_input()
    except (EOFError):
        break
        
    for c in s:
        d = ord(c)
        idx = -1
        if d >= ord('a') and d <= ord('z'):
            idx = d - ord('a')
        if d >= ord('A') and d <= ord('Z'):
            idx = d - ord('A')
        if idx >= 0:
            D[idx] = D[idx] + 1

for i in range(0,26):
    c = chr(i + ord('a'))
    print c + " : " + str(D[i])