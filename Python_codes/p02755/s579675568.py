import math
answer = 0
score = list(map(int,input().split()))
Alist = []
for i in range(2000):
    if math.floor((i+1)*0.08) == score[0]:
        Alist.append(i+1)
for j in range(2000):
    if math.floor((j+1)*0.10) == score[1]:
        if j+1 in Alist:
            print(j+1)
            answer = 1
            break
if answer == 0:
    print(-1)