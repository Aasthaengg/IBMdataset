n = int(input())
creatures = list(map(int, input().split()))

creatures.sort()

accumulation = []

for i in range(len(creatures)):
    if i == 0:
        accumulation.append(0)
    else:
        accumulation.append(creatures[i-1]+accumulation[i-1])
        
creatures.reverse()
accumulation.reverse()

ans = 0

for i in range(len(creatures)):
    if i == 0:
        ans += 1
    else:
        if creatures[i-1] > (creatures[i] + accumulation[i])*2:
            break
        else:
            ans += 1
            
print(ans)