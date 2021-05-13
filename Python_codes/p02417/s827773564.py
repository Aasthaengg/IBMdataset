str = ''
while True:
    try:
        sent = raw_input()
    except:
        break
    str += sent.lower()

for i in range(ord('a'),ord('z')+1):
    print "%s : %d" %(chr(i),str.count(chr(i)))