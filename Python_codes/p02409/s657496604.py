# coding: utf-8
def make_buildings():
    return [[[0 for room in range(10)] for floor in range(3)] for building in range(4)]

def print_building(building):
    return "\n".join(map(lambda floor: " " + " ".join(map(str, floor)),building))
    
line_number = int(input())
regidents_data = [list(map(int, input().split(" "))) for i in range(line_number)]
buildings = make_buildings()

for data in regidents_data:
    b, f, r, v = data
    buildings[b-1][f-1][r-1] += v

print("\n####################\n".join(map(print_building, buildings)))