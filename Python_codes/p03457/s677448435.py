n = int(input())
t = []
p = [0, 0, 0]
while(n):
    a, b, c = input().split(' ')
    t.append([int(a), int(b), int(c)])
    n-=1
for i in t:
    while(p[0] < i[0]):
        p[0]+=1
        if i[1] > p[1]:
            p[1]+=1
        elif i[2] > p[2]:
            p[2]+=1
        elif i[1] < p[1]:
            p[1]-=1
        elif i[2] < p[2]:
            p[2]-=1
        else:
            p[1]-=1
    if p != i:
        print('No')
        exit()
print('Yes')