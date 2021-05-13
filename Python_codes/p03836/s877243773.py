import sys
input = sys.stdin.readline

sx,sy,tx,ty = list(map(int,input().split()))
right = tx - sx
up = ty - sy

go1 = 'R'*right + 'U'*up
back1 =""
for i in range(len(go1)):
    if go1[i] == 'R':
        back1 += 'L'
    elif go1[i] == 'U':
        back1 += 'D'
    elif go1[i] == 'L':
        back1 += 'R'
    elif go1[i] == 'D':
        back1 += 'U'
        
go2 = 'D' + 'R'*(right+1)+'U'*(up+1)+'L'

back2 =""
for i in range(len(go2)):
    if go2[i] == 'R':
        back2 += 'L'
    elif go2[i] == 'U':
        back2 += 'D'
    elif go2[i] == 'L':
        back2 += 'R'
    elif go2[i] == 'D':
        back2 += 'U'

print(go1+back1+go2+back2)
