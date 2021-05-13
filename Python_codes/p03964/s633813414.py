from sys import stdin
from operator import itemgetter
# stdin = open("sample.txt")

N = int(stdin.readline().rstrip())
hyo = [0,0]
ans = [0,0]

for i in range(N):
    hyo[0],hyo[1] = [int(x) for x in stdin.readline().rstrip().split()]

    if ans[0]<=hyo[0] and ans[1]<=hyo[1]:
        ans[0] = hyo[0]
        ans[1] = hyo[1]
    elif ans[0]>hyo[0] and ans[1]>hyo[1]:
        if ans[0]%hyo[0] == 0:
            which1 = ans[0]//hyo[0]
        else:
            which1 = ans[0]//hyo[0]+1
        if ans[1]%hyo[1] == 0:
            which2 = ans[1]//hyo[1]
        else:
            which2 = ans[1]//hyo[1]+1
        if which1 >= which2:
            which = which1
        else:
            which = which2
        ans[0] = hyo[0] * which
        ans[1] = hyo[1] * which
    elif ans[0]>hyo[0]:
        left = ans[0]//hyo[0]
        if ans[0]%hyo[0] == 0:
            ans[0] = hyo[0]*left
            ans[1] = hyo[1]*left
        else:
            ans[0] = hyo[0]*(left+1)
            ans[1] = hyo[1]*(left+1)
    elif ans[1]>hyo[1]:
        right = ans[1]//hyo[1]
        if ans[1]%hyo[1] == 0:
            ans[0] = hyo[0]*right
            ans[1] = hyo[1]*right
        else:
            ans[0] = hyo[0]*(right+1)
            ans[1] = hyo[1]*(right+1)
    # print(ans)

print(ans[0]+ans[1])