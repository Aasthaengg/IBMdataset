import re

i = input()

j = re.sub(r' .*', '', str(i))
k = re.sub(r'\d*\s', '', str(i))

def Even_number(a, b):
    if a*b % 2 == 0:
        print('Even')
    else:
        print('Odd')

Even_number(int(j), int(k))
