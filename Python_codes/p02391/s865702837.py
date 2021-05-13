# coding: utf-8

def getRelation(a, b):
    if a > b: return '>'
    elif a == b : return '=='
    else: return '<'

inputs = raw_input().rstrip().split()
a, b = [int(x) for x in inputs]

print 'a ' + getRelation(a, b) + ' b'