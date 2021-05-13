#n = int(input())
n, k = map(int, input().split())
al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]
dic = {i: False for i in range(1, n+1)}
tel = [1]
bef = 1
tempInd = 1
while True:
    nex = al[bef-1]
    if dic[nex] == False:
        dic[nex] = tempInd
        tel.append(nex)
        bef = nex
        tempInd += 1
    else:
        lastind = dic[nex]-1
        break
tel.remove(1)
if len(tel) >= k:
    ans = tel[k-1]
else:
    repnum = len(tel)-lastind
    k -= len(tel)
    ans = tel[(k-1) % repnum + lastind]
print(ans)
