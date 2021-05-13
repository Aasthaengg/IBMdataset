K=int(input())

S=[str(_) for _ in range(10)]
ans=S[1:]
S_=[]
for i in range(10):
    for s in S:
        if abs(int(s[0])-i)<=1:
            S_.append(str(i)+s)
            if i!=0:
                ans.append(str(i)+s)
            
for _ in range(9):
#     print(_,'=========')
    S=S_.copy()
    S_=[]
    # print(S)
    S_dict={}

    for i in range(10):
        S_dict[i]=[]

    s_zero=0
    for i in range(10):
        for s in S:
            if abs(int(s[0])-i)<=1:
                S_.append(str(i)+s)
                if i!=0:
                    ans.append(str(i)+s)
                    
    if len(ans)>K+10:
        break
                                
print(ans[K-1])