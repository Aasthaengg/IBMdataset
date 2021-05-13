# -*- coding: utf-8 -*-

def answer(s):
    if s.endswith('s'):
        print(s + 'es')
    else:
        print(s + 's')


answer(input())