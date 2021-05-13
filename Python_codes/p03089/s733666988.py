n=int(input())
b=list(map(int, input().split()))

ans=[]
for i in range(n):
    for j in range(len(b)-1, -1, -1):
        if b[j]==j+1:
            ans.append(b.pop(j))
            break
ans=list(reversed(ans))

if len(ans)!=n:
    print(-1)
else:
    for ans_i in ans:
        print(ans_i)

