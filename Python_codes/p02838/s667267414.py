N = int(input())
A = list(map(int,input().split()))
zero_count = [0]*70
one_count  = [0]*70

for a in A:
    count_ = [0]*70
    bin_a = list(bin(a)[2:])
    bin_a.reverse()
    
    for b_idx,b in enumerate(bin_a):
        count_[b_idx] = int(b)
        
#     print(count_)
    
    for c_idx,c in enumerate(count_):
        if c == 0: 
            zero_count[c_idx] += 1
            
        elif c == 1: 
            one_count[c_idx] += 1
            
# print(zero_count,one_count)
ans = 0     

for l in range(70):
    ans += zero_count[l]*one_count[l]*(2**l)
    
print(ans%((10**9)+7))