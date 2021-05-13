import math
def Koch(tops):
    n = len(tops)
    new_tops = [tops[0]]
    for i in range(n-1):
        b = [0,0]
        a = [2*tops[i][0]/3 + tops[i+1][0]/3, 2*tops[i][1]/3 + tops[i+1][1]/3]
        c = [tops[i][0]/3 + 2*tops[i+1][0]/3, tops[i][1]/3 + 2*tops[i+1][1]/3]
        b[0] = (c[0]-a[0])*math.cos(math.radians(60)) - (c[1]-a[1])*math.sin(math.radians(60)) + a[0]
        b[1] = (c[0]-a[0])*math.sin(math.radians(60)) + (c[1]-a[1])*math.cos(math.radians(60)) + a[1]
        new_tops.append(a)
        new_tops.append(b)
        new_tops.append(c)
        new_tops.append(tops[i+1])
    return new_tops

n = int(input())
tops = [[0.,0.],[100.,0.]]
for i in range(n):
    tops = Koch(tops)

for j in range(len(tops)):
    print(*tops[j], sep=' ')

