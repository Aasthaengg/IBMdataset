from collections import defaultdict
N,P = map(int, input().split())
S = list(input()[::-1])
ans = 0
if P == 2:
    for i,s in enumerate(S):    
        if int(s) in [2,4,6,8,0]:
            ans += N - i
elif P == 5:
    for i,s in enumerate(S):    
        if int(s) in [0,5]:
            ans += N - i
else:
    d = defaultdict(int)
    cnt = 0
    d[0] = 1
    for i,s in enumerate(S):
        cnt = (cnt + pow(10,i,P)*int(s))%P
        d[cnt] += 1
    for k in d.keys():
        if d[k] > 1:
            ans += d[k]*(d[k]-1)//2 
print(ans)
