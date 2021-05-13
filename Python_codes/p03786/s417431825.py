N = int(input())
A = [int(x) for x in input().split()]
A.sort()

tmp = A[0]
ans = 1
for i in range(1,N) :
    if A[i] <= tmp*2 :
        ans += 1
    else :
        ans = 1
    tmp += A[i]

print(ans)
