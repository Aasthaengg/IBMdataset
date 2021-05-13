wor = input().upper()
cou = 0

import re
while True :
    tes = input().split()
    if tes[0] == 'END_OF_TEXT': break
    tes = [temp.upper() for temp in tes]
    cou += tes.count(wor)

print(cou)