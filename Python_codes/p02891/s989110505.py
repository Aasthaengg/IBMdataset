s = list(input())
k = int(input())
if len(s) == 1:
    print(k//2)
    exit()
cnt = 0
# ランレングス圧縮
def rle(lst):
    ans = []
    cnt = 1
    ini = lst[0]
    for i in range(1, len(lst)):
        if ini == lst[i]:
            cnt += 1
        else:
            ans.append((ini, cnt))
            cnt = 1
            ini = lst[i]
    ans.append((ini, cnt))
    return ans

sr = rle(s)
if len(sr) == 1:
    print(sr[0][1]*k//2)
    exit()
for i in range(len(sr)):
    if sr[i][1] >= 2:
        cnt += sr[i][1]//2 * k
if sr[0][0] == sr[-1][0]:
    x = sr[0][1]
    y = sr[-1][1]
    cnt -= (x//2 + y//2 - (x+y)//2) *(k-1)
print(cnt)







