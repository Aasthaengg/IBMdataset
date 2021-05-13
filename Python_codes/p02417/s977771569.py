res = []
import string
sam = string.ascii_lowercase

for mak in sam : res.append([mak,0])

import fileinput
for mak in fileinput.input() :
    for tem in mak.lower() :
        num = sam.find(tem)
        if num != -1 : res[num][1] += 1
        
for mak in range(26) : print('{} : {}'.format(res[mak][0],res[mak][1]))