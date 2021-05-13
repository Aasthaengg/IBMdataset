import sys
num = [0 for i in range(26)]
for str in sys.stdin:
    st=str.lower()
    for k in range(len(st)):
        if ord(st[k])<=122 and ord(st[k])>=97:
            num[ord(st[k])-97]+=1
for i in range(26):
    print("{0} : {1}".format(chr(i+97),num[i]))