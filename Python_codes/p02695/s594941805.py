n,m,q = map(int,input().split())

abcd_list = []
for i in range(q):
    abcd_list.append(list(map(int,input().split())))

a = [1]*n
def next_a(a):
    if a[-1] != m:
        a[-1] += 1
    else:
        d = n-1
        while d > 0 and a[d] == m:
            d-=1
        if d < 0:
            return a
        a[d] += 1
        next = a[d]
        for i in range(d,n):
            a[i] = next
max = -1
a[-1] = 0
while sum(a) != n*m:
    next_a(a)
    test = 0
    for i in range(q):
        if a[abcd_list[i][1]-1] - a[abcd_list[i][0]-1] == abcd_list[i][2]:
            test += abcd_list[i][3] 
    if test > max:
        max = test

print(max)