# -*- coding: utf-8 -*-


#----------
N = int(input().strip())
A_list = list(map(int, input().rstrip().split()))
#----------

count=0
for i in A_list:
    if (i % 2) != 0:
        count += 1

if (count % 2) == 0:
    result = "YES"
else:
    result = "NO"

print(result)
