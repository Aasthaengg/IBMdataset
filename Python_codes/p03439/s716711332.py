from sys import exit

n = int(input())
print(0, flush=True)
inl = input()
inr = inl
if inl == "Vacant":
	exit()
print(n//2, flush=True)
#outr = n//2
inm = input()
if inm == "Vacant":
	exit()

outl, outr = 0, n

while True:
	#前半を見るパターン
	if (((outl+outr)//2 - outl) % 2 == 0 and inl != inm) or (((outl+outr)//2 - outl) % 2 == 1 and inl == inm):
		outr = (outl+outr)//2
		print((outl+outr)//2, flush=True)
		inr = inm
		inm = input()
		if inm == "Vacant":
			exit()

	#後半を見るパターン
	else:
		outl = (outl+outr)//2
		print((outl+outr)//2, flush=True)
		inl = inm
		inm = input()
		if inm == "Vacant":
			exit()