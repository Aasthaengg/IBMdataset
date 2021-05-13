def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

import bisect

N=int(input())
list1=divisor(N)
list1=sorted(list1)
value1=(N**0.5)//1
num=bisect.bisect_left(list1,value1)

x=list1[num]
print(int(x+N/x-2))