n = int(input())
A = []
B = []

for _ in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

A.reverse()
B.reverse()

ans = 0
for i in range(n):
    temp = B[i] - ((A[i]+ans) % B[i])
    if temp == B[i]:
        temp = 0
    ans += temp

print(ans)