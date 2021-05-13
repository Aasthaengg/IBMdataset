# coding: utf-8

c_al = [0] * 26

while True:
    try:
        s = input()
        for i in s:
            if i.isalpha():
                c_al[ord(i.lower()) - ord("a")] += 1
    except EOFError:
        break

for i in range(ord("a"),ord("a")+26):
    print("{0} : {1}".format(chr(i),c_al[i - ord("a")]))