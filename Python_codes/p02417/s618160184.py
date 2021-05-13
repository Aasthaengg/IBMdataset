s = ""
while True:
    try:
        sent = raw_input().lower()
    except:
        break
    s += sent

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:

    result = s.count(i)
    print "%s : %d" %(i,result)