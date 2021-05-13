K = int(input())

N = 50
q = K//N
r = K%N

ans = [q+i for i in range(N)]

for i in range(r):
    ans[i] += N
    for j in range(i+1, N):
        ans[j] -= 1
        
for i in range(N):
    ans[i] = str(ans[i])
    
print(N)
print(" ".join(ans))