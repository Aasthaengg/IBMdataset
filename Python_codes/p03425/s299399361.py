N=int(input())
S_dict={'M':0,'A':0,'R':0,'C':0,'H':0}

for n in range(N):
    S = list(input())[0]
    try:
        S_dict[S]+=1
    except:
        pass
S_dict

from itertools import combinations
ans=0
for c_ in combinations(S_dict.keys(),3):
    ans+=S_dict[c_[0]]*S_dict[c_[1]]*S_dict[c_[2]]
print(ans)