import sys

a,b = map(int,sys.stdin.readline().split())

if a == b:
    opr = '=='
elif a > b:
    opr = '>'
elif a < b:
    opr = '<'

print('a '+opr+' b')