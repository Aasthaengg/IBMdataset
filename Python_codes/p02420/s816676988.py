# coding:utf-8
while True:
    str = raw_input()
    if str == '-':
        break
    n = input()
    for i in range(n):
        num = input()
        t = str[num:]
        t += str[:num]
        str = t
        t = ""
    print str


