N = int(input())
S = input()

ans = 0
for i in range(N-1):
    a = [0]*26
    b = [0]*26
    for j in S[0:i+1]:
        if a[ord(j)-ord('a')]==0:
            a[ord(j)-ord('a')]=1
    for j in S[i+1:N]:
        if b[ord(j)-ord('a')]==0:
            b[ord(j)-ord('a')]=1
    subans = 0    
    for i in range(26):
        if a[i]*b[i]==1:
            subans+=1
    ans = max(ans,subans)
    
print(ans)