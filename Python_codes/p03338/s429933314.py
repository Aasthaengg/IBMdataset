N=int(input())
S=input()

ans=0
for i in range(1,N-1):
    a=[0]*26
    for j in range(i):
        a[ord(S[j])-97]|=1
    for j in range(i,N):
        a[ord(S[j])-97]|=2
    ans=max(ans,a.count(3))

print(ans)
