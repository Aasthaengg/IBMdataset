def janken(aite):
    tokuten = 0
    kachi = 1
    if aite[0]=='r':
        tokuten += pa_p
    elif aite[0]=='s':
        tokuten += gu_r
    else:
        tokuten += choki_s
    #print(0,aite[0],tokuten,kachi)
    for i in range(1,len(aite)):
        if aite[i-1]!=aite[i] or kachi==0:
            kachi = 1
            if aite[i]=='r':
                tokuten += pa_p
            elif aite[i]=='s':
                tokuten += gu_r
            else:
                tokuten += choki_s
            #print(i,aite[i],tokuten,kachi)
        else:
            kachi=0
    return tokuten

n,k = map(int,input().split())
gu_r,choki_s,pa_p = map(int,input().split())
t = str(input())
kaisu = {}
memo = [str('') for i in range(k)]
for i in range(n):
    kaisu.setdefault(t[i],0)
    kaisu[t[i]] += 1
    #print(i%k)
    memo[i%k] += t[i]
ans = 0
for i in range(len(memo)):
    ans += janken(memo[i])
#print(kaisu)
print(ans)
