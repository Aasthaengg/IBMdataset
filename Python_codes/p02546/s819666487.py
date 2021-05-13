import math

def solve():
	solve = str(input());
	if solve[-1]=='s':
		solve+="es";
	else:
		solve+="s";
	print(solve);
	#arr = [int(x) for x in input().split()]
solve();

