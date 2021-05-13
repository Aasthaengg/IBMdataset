        
    
N, M = map(int, input().split())

AB = []
for _ in range(N):
    A, B = map(int, input().split())
    AB.append([A, B])

AB.sort()

gelt = 0
drink = 0
for i in range(len(AB)):
    if drink + AB[i][1] <= M:
        drink += AB[i][1]
        gelt += AB[i][0] * AB[i][1]
    else:
        gelt += (M - drink) * AB[i][0]
        break
        
print(gelt)