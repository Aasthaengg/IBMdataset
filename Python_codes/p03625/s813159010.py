n = int(input())
a_L = list(map(int,input().split()))

import collections

L = collections.Counter(a_L)

L = sorted(L.items(),key=lambda x:x[0],reverse=True)

flag = 0
#print(L)
ans = 0
for k,v in L:
    #print(k,v)
    if v>=4:
        ans = max(ans,k**2)

    if v >= 2:
        if flag== 0:
            tmp = k
            flag += 1
        elif flag == 1:
            ans = max(tmp*k,ans)
            #print(tmp*k)
            #print("ans",tmp,k)
            print(ans)
            exit()

print(0)