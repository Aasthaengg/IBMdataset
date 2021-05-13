import collections as c
import sys
H, W = map(int, input().split())
A = (sys.stdin.read()).replace('\n', '')
deck = c.Counter(list(map(str, A)))

is_Hodd = H%2
is_Wodd = W%2

count = list(deck.values())
if is_Hodd and is_Wodd:
	one = 1
	two = H//2 + W//2
	four = (H//2) * (W//2)

	for i in range(len(count)):
		if count[i] >= 4*four:
			count[i] -= 4*four
			four = 0
			break
		else:
			tmp = count[i]//4
			count[i] -= 4*tmp
			four -= tmp
			
	for i in range(len(count)):
		if count[i] >= 2*two:
			count[i] -= 2*two
			two = 0
			break
		else:
			tmp = count[i]//2
			count[i] -= 2*tmp
			two -= tmp

	for i in range(len(count)):
		if count[i] > 0:
			count[i] -= 1
			one = 0

	if four == 0 and two == 0 and one == 0:
		cond = 1
	else:
		cond = 0

elif is_Hodd or is_Wodd:
	if is_Hodd:
		two = W//2
	else:
		two = H//2

	four = (H//2) * (W//2)

	for i in range(len(count)):
		if count[i] >= 4*four:
			count[i] -= 4*four
			four = 0
			break
		else:
			tmp = count[i]//4
			count[i] -= 4*tmp
			four -= tmp
			
	for i in range(len(count)):
		if count[i] >= 2*two:
			count[i] -= 2*two
			two = 0
			break
		else:
			tmp = count[i]//2
			count[i] -= 2*tmp
			two -= tmp

	if four == 0 and two == 0:
		cond = 1
	else:
		cond = 0

else:
	four = (H//2) * (W//2)

	for i in range(len(count)):
		if count[i] >= 4*four:
			count[i] -= 4*four
			four = 0
			break
		else:
			tmp = count[i]//4
			count[i] -= 4*tmp
			four -= tmp

	if four == 0:
		cond = 1
	else:
		cond = 0

if cond:
	print('Yes')
else:
	print('No')