ms = ""
dic = {k: int(0) for k in [chr(i) for i in range(97, 123)]}
while True:
    try:
        inp = input()
        ms += inp
    except:
        break

for i in ms.lower():
    if ord(i) >= 97 and ord(i) <= 122:
        dic[i] += 1

for k, v in sorted(dic.items(), key=lambda x: x[0]):
    print("{0} : {1}".format(k, v))