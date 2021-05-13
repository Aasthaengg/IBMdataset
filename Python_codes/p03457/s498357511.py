n = int(input())
t = []
t.append([0,0,0])
for i in range(n):
    t.append(list(map(int,input().split())))
#print(t)
for i in range(1,n+1):
    time = t[i][0] - t[i-1][0]
    dist = abs(t[i][1] - t[i-1][1])+abs(t[i][2]-t[i-1][2])
    if (dist > time)or(time%2 != dist %2):
        print('No')
        exit()
print('Yes')
