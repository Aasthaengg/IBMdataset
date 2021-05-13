#coding:utf-8
#1_5_D 2015.4.1
#This program outputs multiples of 3 or any numbers with 3 under n. In this program, n is int(input()).

for i in range(int(input())):
    if (i + 1) % 3 == 0 or '3' in str(i + 1):
        print(' ' + str(i + 1), end = '')
print()