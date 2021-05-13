N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
tmp = 0
j = 0
for i in range(len(A)-1):
    if i == 0:
        ans += A[0]
        j += 1
    elif i % 2 == 0:
        ans += tmp
    else:
        tmp = A[j]
        ans+=tmp
        j += 1
print(ans)