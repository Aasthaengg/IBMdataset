s = input()
x,y = map(int,input().split())
l = []
cnt = 0
for i in s:
    if i=='T':
        l.append(cnt)
        cnt = 0
    else:
        cnt+=1
l.append(cnt)
horizontal = l[2::2]
vartical = l[1::2]
horizontal.sort()
horizontal = horizontal[::-1]
vartical.sort()
vartical = vartical[::-1]
x-=l[0]
now_x = 0
now_y = 0
for i in horizontal:
    if now_x<x:
        now_x+=i
    else:
        now_x-=i
for i in vartical:
    if now_y<y:
        now_y+=i
    else:
        now_y-=i
if now_x==x and now_y==y:
    print('Yes')
else:
    print('No')