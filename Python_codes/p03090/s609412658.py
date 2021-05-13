N = int(input())
tmp = N
ans = []
if tmp%2 == 1:
    tmp -= 1
for i in range(1,tmp+1):
    for j in range(1,tmp+1):
        if i < j and j != tmp+1-i:
            ans.append((i,j))
if N%2 == 1:
    for i in range(1,N):
        ans.append((i,N))
print(len(ans))
for i in range(len(ans)):
    print(*ans[i])