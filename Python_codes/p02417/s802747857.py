sequence = ''
while(True):
    try:
        sequence += input()
    except EOFError:
        break

sequence = sequence.lower()
for i in range(ord('a'), ord('z')+1):
    print("%s : %d" % (chr(i), sequence.count(chr(i))))