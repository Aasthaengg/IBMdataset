import sys
#from collections import ChainMap
input()
rp = sys.stdin.readlines()
cm = {}#ChainMap()

for i in rp:
    if i[0] == 'i':
        cm[i[7:]] = 0
    else:
        if i[5:] in cm:
            print('yes')
        else:
            print('no')