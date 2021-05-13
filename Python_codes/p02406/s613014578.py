import re
list = []
n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 or re.search('3', str(i)):
        list.append(str(i))
print('', ' '.join(list))
