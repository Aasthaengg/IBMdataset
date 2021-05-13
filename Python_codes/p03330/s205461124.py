#Brute Force
n, c = map(int, input().split())
D = []
for i in range(c):
    new_line = list(map(int, input().split()))
    D.append(new_line)

C = []
for i in range(n):
    new_line = list(map(lambda x: int(x) - 1, input().split()))
    C.append(new_line)

color_list = [[], [], []]
for i in range(n):
    for j in range(n):
        mod = ((i + 1) + (j + 1)) % 3
        color = C[i][j]
        color_list[mod].append(color)

def change_color_cost(mod, change_color):
    target = color_list[mod]
    total = 0
    for base_color in target:
        total += D[base_color][change_color]
    return total
#print(change_color_cost(1, 1))

def top3(mod):
    min_costs = [[None, float("inf")]] * 3
    for color in range(c):
        cost = change_color_cost(mod, color)
        min_costs.append([color, cost])
        min_costs.sort(key=lambda x: x[1])
        min_costs = min_costs[:3]
    return min_costs
#print(top3(0))

tops = []
for mod in range(3):
    tops.append(top3(mod))
#print(tops)

min_cost = float("inf")
for color0, cost0 in tops[0]:
    for color1, cost1 in tops[1]:
        for color2, cost2 in tops[2]:
            if color0 != color1 and color1 != color2 and color2 != color0:
                min_cost = min(min_cost, cost0 + cost1 + cost2)
print(min_cost)

