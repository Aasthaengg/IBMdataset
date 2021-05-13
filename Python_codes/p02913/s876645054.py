def Z_algo(S):
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0#最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        #i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i+LCP[i-c] < c+LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and S[j] == S[i+j]: j+=1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP

x=int(input())

s=input()
ans=0

for i in range(x):
    t=s[i:]
    lst=Z_algo(t)
    for i,v in enumerate(lst):
        cnt=min(i,v)
        ans=max(ans,cnt)


print(ans)
