N=int(input())

ans=[]
for i in range(1,N//2*2+1):
    for j in range(i+1,N//2*2+1):
        if j==N//2*2-i+1:
            continue
        else:
            ans.append([i,j])
if N%2==1:
    for i in range(1,N):
        ans.append([i,N])

print(len(ans))
for item in ans:
    print(*item)
