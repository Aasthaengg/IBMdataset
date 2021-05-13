#template
def inputlist(): return [int(k) for k in input().split()]
#template
N,K = inputlist()
S = list(input())
li = []
s = S[0]
for i in range(1,N):
    if S[i] == S[i-1]:
        s += S[i]
    else:
        li.append(s)
        s = S[i]
li.append(s)
n = len(li)
dic = {}
indexa = 0
ans = 0
ksum = [0]*n
ksum[0] = len(li[0])
for i in range(1,n):
    ksum[i] = ksum[i-1]+len(li[i])
for i in range(n):
    if li[i][0] == '0':
        indexa +=1
        dic[indexa] = i
if indexa <= K:
    print(N)
    exit()
if K == 1:
    for i in range(1,indexa+1):
        j = dic[i]
        if i == 1:
            m = ksum[j+1]
            ans = max(ans,m)
            continue
        if j == n-1:
            m = ksum[j]-ksum[j-2]
            ans = max(ans,m)
            continue
        else:
            m = ksum[j+1]-ksum[j]+1
            m += ksum[j-1]-ksum[j-2]
            ans = max(m,ans)
else:
    for i in range(K,indexa+1):
        j = dic[i]
        l = dic[i-K+1]
        sup = 0
        inf = 0
        if j == n-1:
            sup = ksum[j]
        if j != n-1:
            sup = ksum[j+1]
        if l != 0:
            inf = ksum[l-2]
        m = sup-inf
        ans = max(ans,m)
print(ans)