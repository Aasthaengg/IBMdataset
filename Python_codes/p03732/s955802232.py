
N,W = map(int,input().split())

dic = {}
dic[0] = 0

for i in range(N):

    odic = dic.copy()

    w,v = map(int,input().split())

    for j in odic:

        if j + w not in dic and j+w <= W:
            dic[j+w] = odic[j] + v

        elif j+w <= W:
            dic[j+w] = max(odic[j]+v,dic[j+w])

ans = 0

for i in dic:
    ans = max(ans,dic[i])

print (ans)

