N = int(input())
ans = []
for i in range(1,N):
    for j in range(i+1,N+1):
        if i+j!=(N//2)*2+1:
            ans.append([i,j])

print(len(ans))
[print(a,b) for a,b in ans]