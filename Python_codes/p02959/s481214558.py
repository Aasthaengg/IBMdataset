N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
monster = 0
hero = 0
for i in range(N):
    allhero = B[i] + hero
    if allhero<=A[i]:
        monster += allhero
        hero = 0
    else:
        monster += A[i]
        if hero>A[i]:
            hero = B[i]
        else:
            hero = allhero-A[i]
    #print(monster,allhero,hero)

if hero>0:
    monster += min(hero,A[N])
print(monster)