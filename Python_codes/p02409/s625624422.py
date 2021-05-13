n = int(input())
data = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
	b,f,r,v = [int(s) for s in input().split(' ')]
	data[b-1][f-1][r-1] += v

while data:
	building = data.pop(0)
	for floor in building:
		rooms = ' ' + ' '.join([str(room) for room in floor])
		print(rooms)
	if data:
		print('####################')