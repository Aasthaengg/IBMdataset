# coding: UTF-8
alfa_list = [chr(i) for i in range(97, 97+26)]
lines = []
count = 0
while(1):
    try:
        lines.append(str(raw_input()).lower())
    except:
        break
for ch in alfa_list:
    print "{0} : {1}".format(alfa_list[count],str(lines).count(ch))
    count += 1

