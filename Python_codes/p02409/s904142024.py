# coding: utf-8

def showBuilding(buildings):
    for i, tou in enumerate(buildings):
        for wow in tou:
            for room in wow:
                print(' ' + str(room), end='')
            print()
        if i != 3:
            print('####################')


if __name__ == '__main__':
    
    buildings = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]
    
    for _ in range(int(input())):
    
        b, f, r, v = map(int, input().split())
    
        if buildings[b - 1][f - 1][r - 1] + v >= 9:
            buildings[b - 1][f - 1][r - 1] = 9
        elif buildings[b - 1][f - 1][r - 1] + v < 0:
            buildings[b - 1][f - 1][r - 1] = 0
        else:
            buildings[b - 1][f - 1][r - 1] += v
    
    showBuilding(buildings)
