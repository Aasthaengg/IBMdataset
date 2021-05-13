import sys
def ISI(): return map(int, sys.stdin.readline().rstrip().split())

s, w =ISI()
if s>w:
	print("safe")
else:
	print("unsafe")
