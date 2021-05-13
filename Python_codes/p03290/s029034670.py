d , g = map(int,input().split())
poi = [tuple(map(int,input().split())) for i in range(d)]
ans = 10**5
for i in range(2**d):
    cou = 0
    ten = 0
    for j in range(d):
        if i >> j & 1 == 1:
            cou += poi[j][0]
            ten += poi[j][1] + (j+1)*100*poi[j][0]
    for j in reversed(range(d)):
        if ten >= g:
            break
        if i >> j & 1 != 1:
            if g - ten > (j+1)*100*(poi[j][0]-1):
                cou += poi[j][0] - 1
                ten += (j+1)*100*(poi[j][0]-1)
            elif g - ten <= (j+1)*100*(poi[j][0]-1):
                cou -= (ten-g)//((j+1)*100)
                ten = g
                break
    if ten >= g:
        ans = min(ans,cou)
print(ans)