###template###
import sys
input = sys.stdin.readline
def mi(): return map(int, input().split())
###template###

s = input().rstrip()

if len(s)==2: print(s)
else: print(s[::-1])

