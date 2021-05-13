#B - Picture Frame 
H,W = map(int,input().split())
a = []
for _ in range(H):
    ai = list(map(str,input()))
    a.append(ai)

b = ['#']*(W+2)

for i in range(H):
    a[i].insert(0,'#')
    a[i].append('#')
print(''.join(b))
for j in a:
    print(''.join(j))
print(''.join(b))