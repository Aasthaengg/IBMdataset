import math

N,H = list(map(int,input().split()))

A=[]
B=[]
for n in range(N):
    a,b = list(map(int,input().split()))
    A.append(a)
    B.append(b)
    
A.sort(reverse=True)
B.sort(reverse=True)
A,B

a_max=A[0]

B_=[]
for b in B:
    if b < a_max:
        break
    B_.append(b)
B=B_

B_sum = [0]
for b in B:
    B_sum.append(B_sum[-1]+b)

ans = 0
for b_sum_idx,b_sum in enumerate(B_sum):
    if b_sum >= H:
        ans = b_sum_idx
        break
        
    ans = b_sum_idx
H = max(0,H - b_sum)

ans += math.ceil(H/a_max)

print(ans)