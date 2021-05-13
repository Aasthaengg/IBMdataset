[n,k] = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]

ls_posi = []#0を含む
ls_nega = []

for i in range(n):
    if x[i] < 0:
        ls_nega.append(-x[i])
    else:
        ls_posi.append(x[i])

ls_nega.reverse()
ans = 10 ** 9

for i in range(k+1):
    #posiから0〜k個, negaからk-posi個
    if i == 0:
        if len(ls_nega) >= k:
            ans = min(ans,ls_nega[k-1])
    elif i == k:
        if len(ls_posi) >= k:
            ans = min(ans,ls_posi[k-1])
    else:
        if len(ls_posi) >= i and len(ls_nega) >= k - i:
            ans = min(ans,ls_posi[i-1] * 2 + ls_nega[k-i-1])
            ans = min(ans,ls_posi[i-1] + ls_nega[k-i-1] * 2)
print(ans)
