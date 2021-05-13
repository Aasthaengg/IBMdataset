from itertools import permutations
N = int(input())

xy = []
for i in range(N):
    xy.append(list(map(int,input().split())))

n = [i for i in range(N)]
sum = 0
for i in permutations(n):
    i = list(i)
    for j in range(N-1):
        sum += ((xy[i[j]][0]-xy[i[j+1]][0])**2 + (xy[i[j]][1]-xy[i[j+1]][1])**2)**(0.5)

fct = 1
for i in range(1,N+1):
    fct *= i

print(sum/fct)