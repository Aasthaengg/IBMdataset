N, T = map(int, input().split())
A = [int(x) for x in input().split()]

minA = A[0]
maxG = 0
ans = 0
for i in range(1,N) :
    if A[i] < minA :
        minA = A[i]
    else :
        if A[i] - minA > maxG :
            maxG = A[i] - minA
            ans = 1
        elif A[i] - minA == maxG :
            ans += 1

print(ans)
