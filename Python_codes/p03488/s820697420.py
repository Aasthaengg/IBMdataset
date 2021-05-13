s = input()
x, y = map(int, input().split())
d = [len(i) for i in s.split('T')]
 
s1 = d[2::2]
s2 = d[1::2]
 
now_x = [0]
now_y = [0]

x -= d[0]

for i in s1:
    nx = set()
    for j in now_x:
        nx.add(j-i)
        nx.add(j+i)
    now_x = nx

for i in s2:
    ny = set()
    for j in now_y:
        ny.add(j-i)
        ny.add(j+i)
    now_y = ny

if x in now_x and y in now_y:
    print('Yes')
else:
    print('No')
