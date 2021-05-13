# -*- coding: utf-8 -*-

s = input()
before = '-'
for i in s:
    if i == before:
        print('Bad')
        exit(0)

    before = i

print('Good')
