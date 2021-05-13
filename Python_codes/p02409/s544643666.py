rooms = []
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])
rooms.append([[0 for i in range(10)] for j in range(3)])

num = int(raw_input())
for i in range(num):
    b,f,r,v = map(int, raw_input().split())
    rooms[b-1][f-1][r-1] += v

for number, room in enumerate(rooms):
    for row in room:
        print ' ' + ' '.join(map(str, row))
    if len(rooms) - 1 > number:
        print('####################')