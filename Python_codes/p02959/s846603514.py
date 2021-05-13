n = int(input())
monsters = list(map(int, input().split()))
braves = list(map(int, input().split()))
destroys = 0
for i in range(n):
    if braves[i] > monsters[i]:
        destroys += monsters[i]
        braves[i] -= monsters[i]

        if braves[i] > monsters[i + 1]:
            destroys += monsters[i + 1]
            monsters[i + 1] = 0
        
        else:
            destroys += braves[i]
            monsters[i + 1] -= braves[i]
    else:
        destroys += braves[i]
print(destroys)
