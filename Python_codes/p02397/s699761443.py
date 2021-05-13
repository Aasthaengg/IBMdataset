l = []
cnt = 0
while 1:
    x = input()
    if x == '0 0':
        break
    l.append(x)
    cnt += 1
for i in range(cnt):
    f = list(map(int,l[i].split()))
    f.sort()
    print(f[0],f[1],sep=' ')
    del f[:]