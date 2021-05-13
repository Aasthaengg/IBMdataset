N = int(input())
A = list(input())
B = list(input())

p = 10**9 + 7

domino = []
d_=''
for d in range(len(A)):
    d_0 = A[d]
    d_1 = B[d]
    if d_ == d_0:
        continue
        
    if d_0 == d_1:
        domino.append(0) # 0:縦
    if d_0 != d_1:
        domino.append(1) # 1:横
    d_ = d_0

ans = 3
if domino[0] == 1:
    ans = 6
    
for d_0,d_1 in zip(domino[:-1],domino[1:]):
    if d_0 == 0:
        ans = ans*2
    elif d_0 == 1:
        if d_1 == 0:
            pass
        else:
            ans = ans*3
    ans = ans % p
ans = ans % p 
print(ans)