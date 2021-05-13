def main():
    
    n = int(input())
    movements = [list(map(int, input().split())) for i in range(n)]
    houses = [[[0 for room in range(10)] for floor in range(3)] for building in range(4)]
    
    for move in movements:
        [b, f, r, v] = move
        houses[b-1][f-1][r-1] += v
    
    for index, building in enumerate(houses):
        for floor in building:
            print(' ' + ' '.join(map(str,floor)))
        if index != 3: print('#'*20)


main()