import sys
a=sys.stdin.readline()
res = [int(i) for i in a.split() if i.isdigit()] 
A,B = [res[i] for i in (0,1)]
if B%2==0 and (B>=2 and B<= 1000) and (A>=0 and A<=100):
	if A>=13:
		print(B)
	elif A>=6 and A<=12:
		print(int(B/2))
	elif A<=5:
		print(0)
else:
	print("Error")