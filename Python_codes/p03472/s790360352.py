N,H = map(int,input().split())

A = []
B = []
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

A.sort(reverse=True)
B.sort(reverse=True)

ans = 0
cnt = 0
while(1):
    if H<=0:
        print(ans)
        exit()
    if cnt==len(B):
        break
    if A[0]>=B[cnt]:
        break
    H-=B[cnt]
    cnt+=1
    ans+=1

if H%A[0]==0:
    res = H//A[0]
else:
    res = H//A[0]
    res += 1

print(ans+res)