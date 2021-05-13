# -*- coding:utf-8 -*-
import math
count = 0
while True:
    try:
        n = int(input())
        if n == 2 or n == 3 or n == 5 or n == 7:
            count += 1
        if n > 3 and n % 2 != 0:
            for i in range(3,int(math.sqrt(n))+1):
                if n % i == 0:
                    break
                elif i == int(math.sqrt(n)):
                    count += 1
    except  EOFError:
        break
print(count)