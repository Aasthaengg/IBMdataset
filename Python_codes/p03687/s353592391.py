from copy import deepcopy
s = input()

ans = 10**10
for i in range(len(s)):
    a = s[i]
    t = deepcopy(s)
    cnt = 0
    
    while len(set(list(t))) !=1:
        
        cnt +=1
        while True:
            S = ""
            for j in range(len(t)-1):
                if (t[j] == a) or (t[j+1] == a):
                    S +=a
                    #print(t,S,j,t[j],t[j+1],a)
                else:
                    S +=t[j]

            else:
                t = deepcopy(S)
                #print(S,cnt)
                break
    ans = min(ans,cnt)
    #print(S,t,i,ans)
print(ans)