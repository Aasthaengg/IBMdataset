#c = [[0 for i in range(3)] for i in range[3]];
c = [[0,0,0],[0,0,0],[0,0,0]];
c[0] = [int(x) for x in input().split()];
c[1] = [int(x) for x in input().split()];
c[2] = [int(x) for x in input().split()];

ans = 'true';

for i in range(1,3) :
    hdiff =  c[0][i] - c[0][i-1];
    for j in range(1,3) :
        if  c[j][i] - c[j][i-1] != hdiff :
            ans = 'false';
            break;

for i in range(1,3) :
    vdiff =  c[i][0] - c[i-1][0];
    for j in range(1,3) :
        if  c[i][j] - c[i-1][j] != vdiff :
            ans = 'false';
            break;            

if(ans == 'true') :
    print('Yes');
else :
    print('No');