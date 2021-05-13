a, b, c, k = map(int, input().split())

if a-k <= 0:
    a_ans = a
    k = k-a
else:
    a_ans = k
    k=0
if b-k <= 0 and k>0:
    b_ans = b
    k = k-b
else:
    b_ans = k
    k=0
if c-k <= 0 and k>0:
    c_ans = c
    k = k-b
else:
    c_ans = k
    
ans = a_ans*1 + b_ans*0 + c_ans*(-1)
print(ans)
