n=int(input())
alist=[]
maxa=0
nextmax=0
maxindex = 573945
for i in range(n):
    tmpa=int(input())
    if tmpa >= maxa:
        nextmax = maxa
        maxa = tmpa
        maxindex = i
    elif tmpa >= nextmax:
        nextmax = tmpa

for j in range(n):
    if j == maxindex:
        print(nextmax)
    else:
        print(maxa)



