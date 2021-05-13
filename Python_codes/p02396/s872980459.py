import sys
line = 999
prm = list()
while line != 0 :
    line = int(sys.stdin.readline())
    prm.append(line)

for i in range(len(prm)):
    if prm[i] == 0 :
        break
    print 'Case ' + str(i+1) + ': ' + str(prm[i])