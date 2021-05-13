# -*- coding : utf-8 -*-

import math

def is_prime_number(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(num):
        if num % i == 0:
            return False
        i = i + 2
    return True

list_num = int(input())
count_prime = 0
for i in range(list_num):
    num = int(input())
    if is_prime_number(num):
        count_prime = count_prime + 1
print(count_prime)