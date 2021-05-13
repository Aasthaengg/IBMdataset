H, W = map(int, input().split())
N = int(input()) #color num
a = list(map(int, input().split()))

color=[]
for i in range(N):
    for _ in range(a[i]):
       color.append(i+1)
#print(color)
answer=[]
for y in range(H):
    answer.append([None]*W)
cursol=0
for y in range(H):
    if y % 2 == 0:
        for x in range(W):
            answer[y][x]=color[cursol]
            cursol+=1
    if y % 2 == 1:
        for x in range(W-1, -1, -1):
            answer[y][x] = color[cursol]
            cursol += 1
#print(answer)
for y in range(H):
    print(' '.join(list(map(str,answer[y]))))
