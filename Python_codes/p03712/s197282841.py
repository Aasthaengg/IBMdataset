h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
l = []
for i in range(h):
    a[i].insert(0,'#')
    a[i].insert(w+1,'#')

for j in range(h+2):
    if j == 0 or j == h+1:
        l.append('#'*(w+2))
    else:
        l.append(a[j-1])
        
for i in range(h+2):
    print(''.join(l[i]))