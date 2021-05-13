import numpy as np
p,q= input().split()
a,b =(int(p), int(q))
ans_list = input().split()
ans_list =np.array(ans_list).astype(float)
#print(ans_list)
ans_list=np.sort(ans_list)[::-1]
#print(ans_list)
if ans_list[b-1] >= sum(ans_list)/4/b:
    print('Yes')
else:
    print('No')