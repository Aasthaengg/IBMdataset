def score(c,s,t,lis):
    ans = 0
    lis = [0]*26
    ans += s[t-1]
    lis[t-1] = 0
    for j in range(26):
        if t-1 != j:
            lis[j] +=  1
            ans -= lis[j]*c[j] 
    return ans,lis

d = int(input())
c = list(map(int,input().split()))
s = [0]*d
for i in range(d):
    s[i] = list(map(int,input().split()))
lis = [0]*26
for i in range(d):
    ans = 0
    z = 0
    L = lis
    q = 0
    for j in range(26):
        y,p = score(c,s[i],j,L)
        if ans < y:
            ans = y
            z = j
            q = p
    print(z+1)
    lis = q