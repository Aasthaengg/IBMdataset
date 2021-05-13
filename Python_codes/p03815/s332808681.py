n = int(input())
tot = n//11
rem = n%11
tot = tot*2
if rem==0:
	print(tot)
elif rem<=6:
	print(tot+1)
else:
	print(tot+2)