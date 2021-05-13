n = int(input())
A = [0]*n
B = [0]*n

for i in range(n):
    a, b = map(int, input().split())
    A[i], B[i] = a, b

ans = 0
temp = 0
for i in reversed(range(n)):
    if (A[i]+temp)%B[i] != 0:
        j = (A[i]+temp)//B[i]
        ans += B[i]*(j+1)-(A[i]+temp)
        temp += B[i]*(j+1)-(A[i]+temp)
print(ans)
