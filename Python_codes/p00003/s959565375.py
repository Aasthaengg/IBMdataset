# coding: utf-8
#Problem Name: Is it a Right Triangle?
#ID: tabris
#Mail: t123037@kaiyodai.ac.jp

n = int(raw_input())
for i in range(n):
    side = sorted(map(int,raw_input().split(' ')))
    if side[0]**2 + side[1]**2 - side[2]**2:
        print 'NO'
    else:
        print 'YES'

'''
Sample Input
3
4 3 5
4 3 6
8 8 8
'''