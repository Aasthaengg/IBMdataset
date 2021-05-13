alphabet = {chr(c):0 for c in range(ord("a"),ord("z")+1)}
s = ""
while True:
    try:
        s += input().lower()
    except:
            break

for i in s:
    if i in alphabet:
        alphabet[i] += 1

for key in range(ord("a"),ord("z")+1):
    ck = chr(key)
    print("%s : %d" % (ck,alphabet[ck]))