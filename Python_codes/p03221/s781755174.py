def get_(i):
    zero_len = 6-len(str(i))
    return '0'*zero_len+str(i)

def get_idx(n,L):
    if len(L)<100:
        left=0
        right=len(L)
    else:    
        left=0
        right=len(L)

        i=0
        while i < 50:
            half=int((left+right)/2)
            if n <= L[half]:
                right = half
            else:
                left = half
            i+=1
        
    if left >= 1:
        left -= 1
        
    for i in range(left,right+1):
        if L[i]==n:
            return i

N,M = list(map(int,input().split()))
N_list=[[] for n in range(N)]
M_list=[]

for m in range(M):
    P,Y=list(map(int,input().split()))
    N_list[P-1].append(Y)
    M_list.append([P,Y])
    
for n in N_list:
    n.sort()
    
for m in M_list:
    p=get_(m[0])
    
    i=get_idx(m[1],N_list[m[0]-1])+1
    i=get_(i)
    
    print(p+i)