N,M = list(map(int,input().split()))
S = list(input())

s_=''
S_=[]

if len(set(S))==1:
    ans = len(S)-1
    
else:
    for s in S:
        if s != s_:
            S_.append(s)
            s_=s

        else:
            S_[-1]+=s

    change_str_dict={'R':'L','L':'R'}
    change_str=change_str_dict[S_[1][0]]

    for m in range(1,min(2*M,len(S_)),2):
        S_[m]=change_str*len(S_[m])

    S_=''.join(S_)
    # print(S_)

    s_=S_[0]
    ans=0
    for s in S_[1:]:
        if s == s_:
            ans+=1
        else:
            s_=s

print(ans)