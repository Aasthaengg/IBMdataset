N = int(input())
A = list(map(int,input().split()))
B = [set() for x in range(N)]

ans = 0
for i in range(N):
    j = A[i] - 1
    if j in B[i] or i in B[j]:
        ans += 1
    else:
        B[i].add(j)
        B[j].add(i)

print(ans)
