###template###
import sys
inp = sys.stdin.readline
def input(): return inp().rstrip()
def mi(): return map(int, input().split())
###template###

s = input()

if len(s)==2: print(s)
else: print(s[::-1])

