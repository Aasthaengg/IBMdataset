def main():
    height, width, difference = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(height)]
    coordinate = [[] for _ in range(height * width + 1)]
    cost = [0 for _ in range(height * width + 1)]
    for i in range(height):
        for j in range(width):
            coordinate[grid[i][j]] = [i, j]
    for i in range(difference + 1, height * width + 1):
        cost[i] += cost[i - difference]
        cost[i] += abs(coordinate[i][0] - coordinate[i - difference][0]) + abs(coordinate[i][1] - coordinate[i - difference][1])
    queries = int(input())
    for _ in range(queries):
        left, right = map(int, input().split())
        print(cost[right] - cost[left])


if __name__ == '__main__':
    main()

