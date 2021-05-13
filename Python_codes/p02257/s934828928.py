#!/usr/bin/env python
# coding: utf-8

def check_pn(num):
    if (num <2):
        return False
    elif (num==2):
        return True

    if (num%2 == 0):
        return False
    i = 3
    while (i <= num/i):
        if num % i == 0:
            return False
        i += 2

    return True


n = int(input())
listdata = []
for i in range(n):
    listdata.append(int(input()))

n=0
for data in listdata:
    ch = check_pn(data)
    n += ch

print (n)


