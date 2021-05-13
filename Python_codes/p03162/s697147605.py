n = int(input())

felicidade = []

for x in range(n):
    felicidade.append(list(map(int,input().split())))

DP = [0,0,0]

if n == 1:
    print(max(felicidade[0]))

else:

    for x in range(3):
        DP[x] = felicidade[0][x]


    for dia in range(1,n):
        m = [0] * 3
        for x  in range(3):#As duas possíveis escolhas são x e y
            for y  in range(3):
                if x != y: #Se elas forem diferentes
                    m[x] = max(m[x], DP[y] + felicidade[dia][x])
        DP = m
    
    print(max(DP))
