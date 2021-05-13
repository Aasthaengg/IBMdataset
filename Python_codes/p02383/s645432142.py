def Nroll(list):
	a = [list[1],list[5],list[2],list[3],list[0],list[4]]
	return a
def Wroll(list):
	a = [list[2],list[1],list[5],list[0],list[4],list[3]]
	return a
dice = list(map(int,input().split()))
roll = str(input())
pos = [0,1,2,3,4,5]
for i in roll:
	if i == "N":
		pos = Nroll(pos)
	elif i == "S":
		pos = Nroll(Nroll(Nroll(pos)))
	elif i == "W":
		pos = Wroll(pos)
	else:
		pos = Wroll(Wroll(Wroll(pos)))
print(dice[pos[0]])
