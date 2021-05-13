import math
import itertools
input_n = int(input())

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
yakusu_list = divisor(input_n)
yakusu_list.sort()

if (len(yakusu_list) % 2) == 1:
  tmp = yakusu_list[len(yakusu_list)//2 + 1 -1] + yakusu_list[-(len(yakusu_list)//2 + 1)]
  print(tmp -2)
else:
  tmp = yakusu_list[len(yakusu_list)//2 - 1] + yakusu_list[-(len(yakusu_list)//2)]
  print(tmp -2)

