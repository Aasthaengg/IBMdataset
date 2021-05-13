N = int(input())

A = []
for i in range(N):
    A.append(int(input()))

b = 1
ans = 0
for i in range(N):
    b = A[b-1]
    ans += 1
    if b == 2:
         print(ans)
         exit()
print(-1)