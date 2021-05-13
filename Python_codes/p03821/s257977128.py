n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for i in range(n)[-1::-1]:
    val = B[i] - (A[i] + ans)%B[i]
    if val == B[i]:
        continue
    ans += val
    
print(ans)