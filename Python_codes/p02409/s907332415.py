sharpNum = 20
roomNum = 10
height = 15
dataNum = int(input())
#building = [[0]*sharpNum] * height
building = [[0] * sharpNum for i in range(height)]

for data in range(dataNum):
    actBuilding = 1
    actRoom = 0
    actFloor = 0
    b,f,r,v = map(int, input().split())
    for floor in range(height):
        actRoom = 0
        if floor%4 == 3:
            actFloor = 0
            actBuilding = actBuilding + 1
            for room in range(sharpNum):
                building[floor][room] = "#"
        else:
            actFloor = actFloor + 1
            
            for room in range(sharpNum):
                if room%2 == 0:
                    building[floor][room] = " "
                else:
                    actRoom = actRoom + 1 
                    if actBuilding == b and actFloor== f and actRoom == r:
                        building[floor][room] = building[floor][room] + v

for floor in range(height):      
    for i in range(len(building[0])):
        print(building[floor][i],end="")
    print("")
