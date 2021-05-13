N,K = map(int,input().split())
A = list(map(int,input().split()))

bit = [0 for _ in range(40)]

for i in range(N):
    s = format(A[i],'040b')
    for j in range(40):
        bit[j] += int(s[j])
        
x = 0
ans = 0

for j in range(40):
    if N-bit[j] > bit[j] and 2**(39-j)+x <= K:
        x += 2**(39-j)
    
for i in range(N):
    ans += x^A[i]
    
print(ans)