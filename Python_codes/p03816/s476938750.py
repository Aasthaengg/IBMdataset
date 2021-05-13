#ランレングス圧縮
def rle(l):
    ret = []
    n = len(l)
    cnt = 1
    for i in range(1,n):
        if l[i - 1] == l[i]:
            cnt+=1
        else:
            ret.append([l[i - 1],cnt])
            cnt = 1
        if i == n - 1:
            ret.append([l[i],cnt])
    return ret

n = int(input())
a = list(map(int,input().split()))

a.sort()

ans = n

r = rle(a)

for i in range(len(r)):
    if r[i][1] % 2 == 0:
        ans-=r[i][1]
        if i != len(r) - 1:
            r[i + 1][1]-=1
    else:
        ans-=r[i][1] - 1
print(ans)
