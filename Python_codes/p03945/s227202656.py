from itertools import groupby

s =list(input())
a = []

for key, value in groupby(s):
    a.append(key)


print(len(a)-1)