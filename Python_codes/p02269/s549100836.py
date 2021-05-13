# -*- coding: utf-8 -*-

dictionary = {}
input_num = int(raw_input())
counter = 0
while counter < input_num:
    command, key = raw_input().split(' ')
    if command[0] == 'i':
        dictionary[key] = None
    else:
        if key in dictionary:
            print 'yes'
        else:
            print 'no'

    counter += 1