a, b = map(int, input().split())

diff = b-a

def tower_height(x):
    return x * (x+1) // 2

west_tower = tower_height(diff-1)
east_tower = tower_height(diff)

print(west_tower-a)

