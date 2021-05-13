import string
az = list(string.ascii_lowercase)
li = [0 for a in range(len(az))]

while True:
    try:
        a = raw_input()
        for b in list(a):
            if b.lower() in az:
                tmp = az.index(b.lower())
                li[tmp] = li[tmp] + 1
    except:
        break

for c in range(len(az)):
    print az[c] + ' : ' + str(li[c])