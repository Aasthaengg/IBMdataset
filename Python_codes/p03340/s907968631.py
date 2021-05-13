N = int(input())
*A, = map(int,input().split())

S = [0]*(N+1)
X = [0]*(N+1)
for i,a in enumerate(A,1):
    S[i] = S[i-1] + a
    X[i] = X[i-1] ^ a

l = 0
r = 0
ans = 0
while r<N:
    s = S[r+1]-S[l]
    x = X[r+1]^X[l]
    if s==x:
        r+=1
    else:
        ans += r-l
        l+=1
while l<N:
    ans += r-l
    l+=1
print(ans)