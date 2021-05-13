BUILDING = 4
FLOOR = 3
ROOM = 10

resident = []
for i in range(BUILDING):
	building = []
	for j in range(FLOOR):
		floor = []
		for k in range(ROOM):
			floor.append(0)
		building.append(floor)
	resident.append(building)

n = input()
for i in range(n):
	b, f, r, v = map(int, raw_input().split())
	resident[b-1][f-1][r-1] += v

for i in range(BUILDING):
	for j in range(FLOOR):
		output_line = ""
		for k in range(ROOM):
			output_line += " " + str(resident[i][j][k])
		print output_line
	if i != BUILDING-1:
		print "####################"