y = ""
while True:
    try:
        c = raw_input().lower()
        y = y + c
    except:
        break

for i in range(ord('a'),ord('z')+1):
    print("{} : {}".format(chr(i),y.count(chr(i))))