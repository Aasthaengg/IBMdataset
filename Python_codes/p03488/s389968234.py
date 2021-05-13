s = input()
x,y = map(int,input().split())
#%%
mx = []
my = []
mx2 = []
my2 = []


cnt = 0
it = 0
firstFlag = (s[0]=='F')
for t in s:
    if t == 'T':
        
        
        if cnt:
            if it%2==0:
                mx.append(cnt)
                mx2.append(cnt*2)
            else:
                my.append(cnt)
                my2.append(cnt*2)
        it += 1
        cnt = 0
    else:
        cnt += 1
    
if it%2==0:
    mx.append(cnt)
    mx2.append(cnt*2)
else:
    my.append(cnt)
    my2.append(cnt*2)

if firstFlag:
    x -= mx[0]
    mx[0] = 0
    mx2[0] = 0
        
dx = sum(mx)-x
dy = sum(my)-y


# dp[i+1][j] : i個目までの要素の和でjを作れるか？

MAX = max(sum(mx2),sum(my2)) + 10
dpx = [[False]*MAX for _ in range(len(mx2)+1)]
dpy = [[False]*MAX for _ in range(len(my2)+1)]

dpx[0][0] = True
dpy[0][0] = True

for i in range(len(mx2)):
    for j in range(MAX):
        if j<mx2[i]:
            dpx[i+1][j] = dpx[i][j]
        else:
            dpx[i+1][j] = dpx[i][j-mx2[i]] or dpx[i][j]

for i in range(len(my2)):
    for j in range(MAX):
        if j<my2[i]:
            dpy[i+1][j] = dpy[i][j]
        else:
            dpy[i+1][j] = dpy[i][j-my2[i]] or dpy[i][j]



if dx<0 or dy<0:
    print('No')

elif dx>sum(mx2) or dy>sum(my2):
    print('No')

else:
    if dpx[len(mx2)][dx] and dpy[len(my2)][dy]:
        print('Yes')
    else:
        print('No')
        







