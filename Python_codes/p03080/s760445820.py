n = int(input())
s = input()
r = 0
b = 0

for i in s:
    if i == "R":
        r += 1
    elif i== "B":
        b += 1
    else:
        pass
    pass

if r > b:
  	print('Yes')
else:
	print('No')
