#input
S = input()

#slice
Batsu = int(S.count('x'))
Nokori = 15 - Batsu

#output
if Batsu >= 8:
	print("NO")
else:
	print("YES")