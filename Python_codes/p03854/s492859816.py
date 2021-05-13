S = list(input())
S.reverse()

D = [['m','a','e','r','d'],['r','e','m','a','e','r','d'],['e','s','a','r','e'],['r','e','s','a','r','e']]
can = True

while len(S) != 0:
    can2 = False
    for i in range(4):
        d = D[i]
        if S[:len(d)] == d:
            can2 = True
            for j in range(len(d)):
                S.pop(0)
            break
    if can2 == False:
        can = False
        break

if can == True:
    print('YES')
elif can == False:
    print('NO')