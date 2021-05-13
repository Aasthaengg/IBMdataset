s = input()
t = input()
sl = len(s)
st = len(t)
if sl+1 != st:
	print("No")
	exit()

if s != t[:sl]:
	print("No")
	exit()

print("Yes")