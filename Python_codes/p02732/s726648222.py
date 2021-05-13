from collections import Counter

N = int(input())
A = list(map(int,input().split()))

C=Counter(A)

C_={}
sum_ = 0
for k in C.keys():
    c=C[k]
    if c == 1:
        C_[k]=0
    else:
        C_[k]=(c*(c-1))//2
        
    sum_ += C_[k]

for a in A:
    ans = sum_-(C[a]-1)
    print(ans)