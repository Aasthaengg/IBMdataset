s = input()

import string
a = list(string.ascii_lowercase)

for item in a:
    if item not in s:
        print(item)
        break
else:
    print('None')
