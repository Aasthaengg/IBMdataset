dbflag=""

def debug(*args):
	if ""!=dbflag: print(*args)

if ""!=dbflag: _INDATA=open(dbflag)

def readline():
	if ""!=dbflag:return _INDATA.readline()
	else: return input()


result = 0

A,B,C,D = map(int, readline().split())



x = A+B -(C+D)
if x > 0:
	result="Left"
elif x == 0:
	result ="Balanced"
else:
	result="Right"


print(result)
