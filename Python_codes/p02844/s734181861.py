N = int(input())
S =list(str(input()))
a=[]
ans=0
for i in range(10):
    for u in range(10):
        for y in range(10):
            moji=[str(i),str(u),str(y)]
            ti=0
            for t in range(N):
                if S[t]==moji[ti]:
                    ti+=1
                    if ti==3:
                        break
            if ti==3:
                ans+=1
                            
                
print(ans)