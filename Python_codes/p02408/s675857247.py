n = int(input())

cards = {

"S" : list(0 for q in range(13)),
"H" : list(0 for w in range(13)),
"C" : list(0 for e in range(13)),
"D" : list(0 for r in range(13)),

}

for _ in range(n):
	a,b = input().split()
	cards[a][int(b)-1] = 1
for a in ("S", "H", "C", "D"):
	for b in range(13):
		if cards[a][b] == 0:
			print(a,b+1)