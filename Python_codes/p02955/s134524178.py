N,K = map(int, input().split())
A = [int(a) for a in input().split()]

M = sum(A)
L = []
i = 1
while i <= M**0.5:
    if M%i == 0:
        L.append(i)
        L.append(M//i)
    i += 1
    
L.sort(reverse=True)

for i in L:
    temp = [0]*N
    for j in range(N):
        temp[j] = A[j]%i
    temp.sort()
    cnt = 0
    l = 0
    r = N-1
    while l < r:
        if temp[l] == 0:
            l += 1
            continue
        if temp[r] == 0:
            r -= 1
            continue
        t = temp[l]
        temp[l] = 0
        cnt += t
        while l < r and temp[r]+t > i:
            t -= i-temp[r]
            temp[r] = 0
            r -= 1
        temp[r] += t
        temp[r] %= i
            
    if cnt <= K:
        ans = i
        break

print(ans)