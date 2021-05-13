S=list(input())
K=int(input())

S_=[]
for s in range(len(S)):
    s_temp=S[s]
    S_.append(s_temp)
    for e in range(s+1,len(S)):
        if e-s>K+10:
          break
        s_temp+=S[e]
        S_.append(s_temp)
        
S_=list(set(S_))
S_.sort()
# print(S_)
print(S_[K-1])