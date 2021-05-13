sx,sy, tx,ty = map(int, raw_input().split())
def f(sx,sy,tx,ty):
	path = ['D']
	path += ['R'] * (abs(tx - sx) + 1)
	path += ['U'] * (abs(ty - sy) + 1)
	path += ['L'] * (abs(tx - sx) + 1)
	path += ['D'] * (abs(ty - sy))
	return path

	
def g(sx,sy,tx,ty):
	path = []
	path += ['R'] * (abs(tx - sx))
	path += ['U'] * (abs(ty - sy) + 1)
	path += ['L'] * (abs(tx - sx)+1)
	path += ['D'] * (abs(ty - sy)+1) 
	return path + ['R']


print ''.join(f(sx,sy, tx,ty) + g(sx,sy,tx,ty))
