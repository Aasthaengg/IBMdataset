s = ""
while True:
    try:
        x = raw_input().lower()
    except:
        break
    s += x

for i in range(26):
    c = chr(i + ord('a'))
    print('%s : %d' %(c, s.count(c)))