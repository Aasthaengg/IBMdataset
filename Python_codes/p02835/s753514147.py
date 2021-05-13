import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())
a, b, c=ISI()
if a+b+c>21:print("bust")
else:print("win")