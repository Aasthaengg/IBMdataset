from itertools import zip_longest
O = input()
E = input()
print(''.join(S+T for S,T in zip_longest(O,E,fillvalue='')))