N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

d = {i:[] for i in range(K)}
score = {"r":P, "s":R, "p":S}

for i in range(len(T)):
    d[i%K].append(T[i])
  
ans = 0
cnt = 1
for val in d.values():
    cnt = 1
    for i in range(len(val)-1):
        if(val[i] == val[i+1]):
            cnt += 1
            
        else:
            if(cnt > 1):
                if(cnt%2 == 0):
                    ans += score[val[i]]*(cnt//2)
                    cnt = 1
                else:
                    ans += score[val[i]]*(cnt//2+1)
                    cnt = 1
            else:
                ans += score[val[i]]
    if(cnt > 1):
        if(cnt%2 == 0):
            ans += score[val[i]]*(cnt//2)
        else:
            ans += score[val[i]]*(cnt//2+1)
    
    else:
        ans += score[val[-1]]
    
print(ans)