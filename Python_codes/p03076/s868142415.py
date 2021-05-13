A = [int(input()) for _ in range(5)]
ans = 0
temp2 = 10

for i in range(5):
    if A[i] % 10 == 0:
        ans += A[i]
    else:
        temp = (A[i]//10)*10 + 10
        ans += temp
        if temp2 > A[i] % 10:
            temp2 = A[i] % 10


temp2 = 10 - temp2
ans = ans - temp2
print(ans)
