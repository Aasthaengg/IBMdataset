N = int(input())
S = list(input())

def get_ans(ans_,c):
    if c < 0:
        pass
    else:
        ans_ -= B_[c]
    return ans_

# N=4000
# S=[random.choice(['R','G','B']) for _ in range(N)]

S_dict={'R':set(),'G':set(),'B':set()}
for s_idx,s in enumerate(S):
    S_dict[s].add(s_idx+1)
    
# print(S_dict)
B_ = [0]*(2*N)
for s_b in S_dict['B']:
    B_[s_b]=1
    
S_R=S_dict['R']
S_G=S_dict['G']
    
ans=0
ans__=len(S_dict['B'])
for s_r in S_R:
    for s_g in S_G:
        ans_=ans__
        c_= abs(s_r-s_g)
        c_mean = 0
        if (s_r + s_g)%2 == 0:
            c_mean = (s_r + s_g)//2
            ans_ = get_ans(ans_,c_mean)
            
#         print('=====')
#         print(s_r,s_g,c_,c_mean)
        
        if s_r > s_g:
            ans_ = get_ans(ans_,s_r + c_)
            ans_ = get_ans(ans_,s_g - c_)
            
#             print(s_r + c_,s_g - c_)
            
        else:
            ans_=get_ans(ans_,s_r - c_)
            ans_=get_ans(ans_,s_g + c_)
            
#             print(s_r - c_,s_g + c_)
        
        ans+=ans_
        
#         print(ans_,ans)
        
print(ans)