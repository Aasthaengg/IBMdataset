# coding=utf-8

n = int(raw_input())
cards = {'S':[], 'H':[], 'C':[], 'D':[]}
for _ in xrange(n):
    mark, num = raw_input().split()
    cards[mark].append(num)
for mark in ['S', 'H', 'C', 'D']:
    for i in xrange(1, 14):
        if str(i) not in cards[mark]:
            print mark + ' ' + str(i)