import math
N  = int(input())
左端 = [False] * (N + 1)
参照 = [False] * (N + 1)
places = [-1] * ( N + 1)
for ind in range(N):
    temp = int(input())
    places[temp] = ind
for num in range( 1,N + 1):
    if 参照[num] == False:
        左端[num] = True
        l = 1
        while True:
            if num + l <= N and places[num+ l - 1] < places[num + l]:
                参照[num + l] = True
                l += 1
            else:
                break

hoge = 0
for i in range(1 ,N  + 1):
    if 左端[i]:
        cot = 1
        l = i + 1
        while True:
            if l <= N and 参照[l]  :
                cot += 1
                l += 1
            else:
                break
        hoge = max(cot,hoge)
print(N - hoge)