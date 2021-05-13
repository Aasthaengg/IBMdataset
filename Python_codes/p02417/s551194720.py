s = ""
while True:
    try:
        x = raw_input()
    except:
        break
    s += x
s = s.lower()

for i in range(26):
    c = chr(i + ord('a'))
    print('%s : %d' %(c, s.count(c)))