N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

eriminate_enemy = [0 for _ in range(N+1)]

for index, B in enumerate(Bs):
    if(B <= As[index]):
        eriminate_enemy[index] += B
        continue

    eriminate_enemy[index] += As[index]
    
    if(B <= As[index] + As[index + 1]):
        eriminate_enemy[index + 1] += B - As[index]
        As[index+1] -= eriminate_enemy[index + 1]
    
    else:
        eriminate_enemy[index + 1] += As[index+1] 
        As[index+1] = 0

print(sum(eriminate_enemy))

