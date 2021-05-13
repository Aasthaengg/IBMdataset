import sys
alf = []
countchan = []
for i in range(26):
    alf.append(chr(ord("a")+i))
    countchan.append(0)
for i in sys.stdin.readlines():
    for i2 in range(26):
        countchan[i2] += i.count(chr(ord("a")+i2))
        countchan[i2] += i.count(chr(ord("A")+i2))
for i in range(26):
    print(alf[i]+" : "+str(countchan[i]))