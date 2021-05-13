import sys
sys.setrecursionlimit(10**9)

H, W = map(int, input().split())
field = [input() for i in range(H)]
route_count_memory = [[-1] * W for i in range(H)]
route_count_memory[0][0] = 1

def get_route_count(i,j):
    result = 0
    if route_count_memory[i][j] != -1:
        return route_count_memory[i][j]
    if 0 <= i-1 < H and field[i-1][j] != '#':
        result += get_route_count(i-1, j)
    if 0 <= j-1 < W and field[i][j-1] != '#':
        result += get_route_count(i, j-1)
    route_count_memory[i][j] = result
    return result

print(get_route_count(H-1, W-1)%(10**9+7))
