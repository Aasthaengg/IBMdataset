N = int(input())
A = list(map(int,input().split()))

B = [0] * N
M = 0
ans = []
for i in range(N,0,-1):
    S, idx = 0, i-1
    while idx <= N-1:
        S += B[idx]
        idx += i

    if S % 2 != A[i-1]:
        B[i-1] = 1
        M += 1
        ans.append(i)
        

print(M)
for a in ans:
    print(a, end=" ")
print("")